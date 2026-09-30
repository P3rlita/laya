from laya import Router

def main():
    print("Demo clasifiación de cerveza")

    router = Router()

    text = "Quiero una cerveza ligera y refrescante para tomar con tacos de pesca."

    questions = {
        "categoria":{
            "type": "choice",
            "instructions": "Clasifica la cerveza que mejor se encaje al texto.",
            "criteria": {
                "lager": "Cerveza ligera y refrescante, de color claro y sabor suave.",
                "ipa": "Cerveza amarga, lupulada y aromantica",
                "stout" : "cerveza oscura, con sabor a malta tostada y notas de chocolate o café.",
                "trigo": "Cerveza suave, fresca y con notas de pan o especias."
            }
        }
    }
    result = router.predict({"text": text}, questions)
    answers = result["answers"]["categoria"]

    print("Texto:", text)
    print("Categoría:", answers["choice"])

    if "confidence" in answers:
        print("Confianza:", round(answers["confidence"], 3))

    print("Modelo:", result["routing"]["model"])

if __name__ == "__main__":
    main()