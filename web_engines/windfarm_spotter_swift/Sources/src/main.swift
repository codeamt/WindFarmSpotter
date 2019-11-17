import Foundation
import PythonKit
import Kitura
import SwiftyJSON
import Path
import CoreImage


let srcroot = (ProcessInfo.processInfo.environment["SRCROOT"] ?? "unwrapped")
let sys = Python.import("sys")
sys.path.insert(0, srcroot + "/python/site-packages")
print("Using Python Version: ", Python.versionInfo)

//<--------- PY IMPORTS ----------->
let torch:PythonObject! = Python.import("torch")
let torchvision:PythonObject! = Python.import("torchvision")
let fastai:PythonObject! = Python.import("fastai")
let vision:PythonObject! = Python.import("fastai.vision")
let io:PythonObject! = Python.import("io")
let time:PythonObject! = Python.import("time")
let base64 = Python.import("base64")
let PIL = Python.import("PIL")
let np = Python.import("numpy")
_ = Python.import("pytorchcv")





//to resolve issues with chaining methods
let BytesIO = io.BytesIO
let Image = vision.Image
let Learner = vision.Learner
let path = Path(srcroot + "/model")!.string
let model_path = Path(srcroot + "/model/effnet-b1-c98.pkl")!.string


//<---------- MODEL DEFINITION ------->
struct WindfarmSpotter {
    let model = vision.load_learner(path: path, file: model_path)
    
    let prediction_labels:[String:[String:String]] = [
        "turbines_low_capacity" : ["label": "Low Capacity Wind Farm", "CO2": ""],
        "turbines_med_capacity" : ["label": "Medium Capacity Wind Farm", "CO2": ""],
        "turbines_high_capacity" : ["label": "High Capacity Wind Farm", "CO2": ""],
        "no_turbines_no_potential" : ["label": "Not a Turbine Farm", "CO2": ""],
        "no_turbines_low_potential" : ["label": "Potential Low Capacity Wind Farm", "CO2": ""],
        "no_turbines_med_potential" : ["label": "Potential Medium Capacity Wind Farm", "CO2": ""],
        "no_turbines_high_potential" : ["label":"Potential High Capacity Wind Farm", "CO2": ""]
    ]
    
    func PIL2numpy(path:String) -> PythonObject? {
        let bytes = io.BytesIO(base64.b64decode(path))
        let img:PythonObject = vision.image.open_image.dynamicallyCall(withArguments: [bytes as PythonConvertible])
        return img
    }
    
    func predict(data:PythonObject) -> PythonObject {
        return self.model.predict(data)
    }
    
}

let windfarm_spotter = WindfarmSpotter()


//<-------------  ROUTING ------------>
let router = Router()
router.all(middleware: BodyParser())


//index
router.get("/") { request, response, next in
    response.send("The server is up and running. project path is.")
    next()
}

//re-training service
router.get("/retrain") { request, response, next in
    response.send("NotImplemented")
    next()
}

router.get("/predict") { request, response, next in
     if let incoming = request.body {
        let fn = incoming.asJSON?["img"] as! String
        let path = Path(fn)!
        let data = try! Data(contentsOf: path.url)
        let input = windfarm_spotter.PIL2numpy(path: data.base64EncodedString())
        let start_time = time.time()
        let output = windfarm_spotter.predict(data: input!).tuple3
        print(output.0)
        let time_delta = time.time() - start_time
        _ = Python.builtins
        let label:String = String(output.0.self.__str__())!
        let json_prediction:[String: String ] = [
            "CLASSS": windfarm_spotter.prediction_labels[label]!["label"]!,
            "INFERENCE TIME": String(Float(time_delta)!) + " seconds"
        ]
        print(JSON(json_prediction))
        response.send(JSON(json_prediction))
        next()
     } else {
        response.status(.badRequest)
        next()
    }
}


//start server
Kitura.addHTTPServer(onPort: 3333, with: router)
Kitura.run()






