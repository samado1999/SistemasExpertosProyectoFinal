from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ExpertSystems.models import symptoms, expertreponse
from ExpertSystems.serializers import symptomsSerializer, expertreponseSerializer

import os
from experta import *

# Create your views here.
# get method
@csrf_exempt
def disease_list(request):
    if request.method == "GET":
        # diseases = disease.objects.all()
        # serializer = diseaseSerializer(diseases, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return JsonResponse({"message": "GET request not supported"}, status=400)
    elif request.method == "POST":
        # data = JSONParser().parse(request)
        # serializer = diseaseSerializer(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(serializer.data, status=201)
        # return JsonResponse(serializer.errors, status=400)
        preprocess()
        data = JSONParser().parse(request)
        serializer = symptomsSerializer(data=data)
        if serializer.is_valid():
            res_gender = serializer.data.get("gender")
            print("GENDER: " + res_gender)
            res_age = float(serializer.data.get("age"))
            res_pas_no_trat = float(serializer.data.get("pas_no_trat"))
            res_pas_trat = serializer.data.get("pas_trat")
            res_diabetes = serializer.data.get("diabetes")
            res_smoking_status = serializer.data.get("smoking_status")
            res_ecv = serializer.data.get("ecv")
            res_fa = serializer.data.get("fa")
            res_hvi = serializer.data.get("hvi")

            global var1, var2, var3, var4, var5, var6, var7, var8, var9
            global points_pas, points_diabetes, points_smoking_status, points_ecv, points_fa, points_hvi

            var1 = "yes" if res_gender != "" else "no"  # Género
            var2 = "yes" if res_age >= 82 else "no"  # Edad
            var3 = (
                "yes" if res_pas_no_trat >= 205 else "no"
            )  # Presión arterial sistólica (no tratada)

            var4 = (
                "yes" if res_pas_trat == "1" else "no"
            )  # Presión arterial sistólica (tratada con medicamentos)

            # pas no tratada, res_pas_no_trat / res_pas_trat, mujer
            if (
                res_pas_trat == "0"
                and (res_pas_no_trat >= 95 and res_pas_no_trat <= 106)
                and res_gender == "hombre"
            ):
                points_pas = 1
            elif (
                res_pas_trat == "0"
                and (res_pas_no_trat > 106 and res_pas_no_trat <= 120)
                and res_gender == "hombre"
            ):
                points_pas = 2
            elif (
                res_pas_trat == "0"
                and (res_pas_no_trat > 120 and res_pas_no_trat <= 130)
                and res_gender == "hombre"
            ):
                points_pas = 3
            elif (
                res_pas_trat == "0"
                and (res_pas_no_trat > 130 and res_pas_no_trat <= 140)
                and res_gender == "hombre"
            ):
                points_pas = 4
            elif (
                res_pas_trat == "0"
                and (res_pas_no_trat > 140 and res_pas_no_trat <= 160)
                and res_gender == "hombre"
            ):
                points_pas = 5
            elif (
                res_pas_trat == "0"
                and (res_pas_no_trat > 160 and res_pas_no_trat <= 180)
                and res_gender == "hombre"
            ):
                points_pas = 6
            elif (
                res_pas_trat == "0"
                and (res_pas_no_trat > 180 and res_pas_no_trat <= 200)
                and res_gender == "hombre"
            ):
                points_pas = 7
            elif (
                res_pas_trat == "0"
                and (res_pas_no_trat > 200 and res_pas_no_trat <= 220)
                and res_gender == "hombre"
            ):
                points_pas = 8
            elif (
                res_pas_trat == "0"
                and (res_pas_no_trat > 220 and res_pas_no_trat <= 240)
                and res_gender == "hombre"
            ):
                points_pas = 9
            elif (
                res_pas_trat == "1"
                and (res_pas_no_trat > 95 and res_pas_no_trat <= 106)
                and res_gender == "hombre"
            ):
                points_pas = 1
            elif (
                res_pas_trat == "1"
                and (res_pas_no_trat > 106 and res_pas_no_trat <= 120)
                and res_gender == "hombre"
            ):
                points_pas = 2
            elif (
                res_pas_trat == "1"
                and (res_pas_no_trat > 120 and res_pas_no_trat <= 130)
                and res_gender == "hombre"
            ):
                points_pas = 3
            elif (
                res_pas_trat == "1"
                and (res_pas_no_trat > 130 and res_pas_no_trat <= 140)
                and res_gender == "hombre"
            ):
                points_pas = 4
            elif (
                res_pas_trat == "1"
                and (res_pas_no_trat > 140 and res_pas_no_trat <= 160)
                and res_gender == "hombre"
            ):
                points_pas = 5
            elif (
                res_pas_trat == "1"
                and (res_pas_no_trat > 160 and res_pas_no_trat <= 180)
                and res_gender == "hombre"
            ):
                points_pas = 6
            elif (
                res_pas_trat == "1"
                and (res_pas_no_trat > 180 and res_pas_no_trat <= 200)
                and res_gender == "hombre"
            ):
                points_pas = 7
            elif (
                res_pas_trat == "1"
                and (res_pas_no_trat > 200 and res_pas_no_trat <= 220)
                and res_gender == "hombre"
            ):
                points_pas = 8
            elif (
                res_pas_trat == "1"
                and (res_pas_no_trat > 220 and res_pas_no_trat <= 240)
                and res_gender == "hombre"
            ):
                points_pas = 9

            
            #
            if (
                res_pas_trat == "0"
                and (res_pas_no_trat >= 95 and res_pas_no_trat <= 106)
                and res_gender == "mujer"
            ):
                points_pas = 1
            elif (
                res_pas_trat == "0"
                and (res_pas_no_trat > 106 and res_pas_no_trat <= 120)
                and res_gender == "mujer"
            ):
                points_pas = 2
            elif (
                res_pas_trat == "0"
                and (res_pas_no_trat > 120 and res_pas_no_trat <= 130)
                and res_gender == "mujer"
            ):
                points_pas = 3
            elif (
                res_pas_trat == "0"
                and (res_pas_no_trat > 130 and res_pas_no_trat <= 140)
                and res_gender == "mujer"
            ):
                points_pas = 4
            elif (
                res_pas_trat == "0"
                and (res_pas_no_trat > 140 and res_pas_no_trat <= 160)
                and res_gender == "mujer"
            ):
                points_pas = 5
            elif (
                res_pas_trat == "0"
                and (res_pas_no_trat > 160 and res_pas_no_trat <= 180)
                and res_gender == "mujer"
            ):
                points_pas = 6
            elif (
                res_pas_trat == "0"
                and (res_pas_no_trat > 180 and res_pas_no_trat <= 200)
                and res_gender == "mujer"
            ):
                points_pas = 7
            elif (
                res_pas_trat == "0"
                and (res_pas_no_trat > 200 and res_pas_no_trat <= 220)
                and res_gender == "mujer"
            ):
                points_pas = 8
            elif (
                res_pas_trat == "0"
                and (res_pas_no_trat > 220 and res_pas_no_trat <= 240)
                and res_gender == "mujer"
            ):
                points_pas = 9
            elif (
                res_pas_trat == "1"
                and (res_pas_no_trat > 95 and res_pas_no_trat <= 106)
                and res_gender == "mujer"
            ):
                points_pas = 1
            elif (
                res_pas_trat == "1"
                and (res_pas_no_trat > 106 and res_pas_no_trat <= 120)
                and res_gender == "mujer"
            ):
                points_pas = 2
            elif (
                res_pas_trat == "1"
                and (res_pas_no_trat > 120 and res_pas_no_trat <= 130)
                and res_gender == "mujer"
            ):
                points_pas = 3
            elif (
                res_pas_trat == "1"
                and (res_pas_no_trat > 130 and res_pas_no_trat <= 140)
                and res_gender == "mujer"
            ):
                points_pas = 4
            elif (
                res_pas_trat == "1"
                and (res_pas_no_trat > 140 and res_pas_no_trat <= 160)
                and res_gender == "mujer"
            ):
                points_pas = 5
            elif (
                res_pas_trat == "1"
                and (res_pas_no_trat > 160 and res_pas_no_trat <= 180)
                and res_gender == "mujer"
            ):
                points_pas = 6
            elif (
                res_pas_trat == "1"
                and (res_pas_no_trat > 180 and res_pas_no_trat <= 200)
                and res_gender == "mujer"
            ):
                points_pas = 7
            elif (
                res_pas_trat == "1"
                and (res_pas_no_trat > 200 and res_pas_no_trat <= 220)
                and res_gender == "mujer"
            ):
                points_pas = 8
            elif (
                res_pas_trat == "1"
                and (res_pas_no_trat > 220 and res_pas_no_trat <= 240)
                and res_gender == "mujer"
            ):
                points_pas = 9

            var5 = "yes" if res_diabetes == "1" else "no"  # Diabetes
            points_diabetes = 3 if res_diabetes == "1" else 0  # Diabetes

            var6 = "yes" if res_smoking_status == "1" else "no"  # Fumador
            points_smoking_status = 3 if res_smoking_status == "1" else 0  # Fumador

            var7 = "yes" if res_ecv == "1" else "no"  # Enfermedades cardiovasculares
            points_ecv = 2 if res_ecv == "1" else 0  # Enfermedades cardiovasculares

            var8 = (
                "yes" if res_fa == "1" else "no"
            )  # Antecedentes de fibrilación auricular
            points_fa = (
                6 if res_fa == "1" else 0
            )  # Antecedentes de fibrilación auricular

            var9 = (
                "yes" if res_hvi == "1" else "no"
            )  # Diagnóstico de hipertrofia ventricular izquierda
            points_hvi = (
                4 if res_hvi == "1" else 0
            )  # Diagnóstico de hipertrofia ventricular izquierda

            # sum points
            points = (
                points_diabetes
                + points_smoking_status
                + points_ecv
                + points_fa
                + points_hvi
            )
            print("points: " + str(points))

            # id_disease_response = "no_disease"
            # description_response = "no_description"
            # treatment_response = "no_treatment"
            preprocess()
            make_engine()

            # return expertreponseSerializer
            return JsonResponse(
                {
                    "description": id_disease_response,
                    "symptoms": description_response,
                    "treatment": treatment_response,
                },
                status=201,
            )
        return JsonResponse(serializer.errors, status=400)


diseases_list = []
diseases_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}
"""
PROBABILIDAD DE QUE UN PACIENTE SUFRA UN ATAQUE CEREBRO VASCULAR EN 10 AÑOS

Debido a que la probabilidad de sufrir un ataque cerebrovascular está sujeta a diferentes variable o características,
se tomaran las principales de estás, que como se ha descrito en los avances del proyecto, son;

Características con mayor peso:
    - Genero (masculino/femenino)
    - Edad (segmentar en: menor/mediano/mayor)
    - Hipertensión (sí/no)
    - Enfermedad del corazón (sí/no)
    - Nivel medio de glucosa (porcentaje/n/a)
    - Índice de masa corporal, es igual a: peso / (estatura * estatura (m))
    - Ha sufrido alguna vez de un ataque cerebro vascular? (sí/no)
    - Ha fumado? (siempre/de vez en cuando/nunca)
    - Presión arterial sistólica
    - Diabetes (sí/no)
    
    - gender
    - age
    - pas-no-trat
    - pas-trat
    - diabetes
    - smoking_status
    - ecv (enfermedad cardiovascular)
    - fa (antecedentes de fibrilación auricular)
    - hvi (diagnóstico de hipertrofia ventricular izquierda)
    
Se hará uso de la tabla expuesta por NINDS para calcular el riesgo de padecer un accidente vascular celebral.

en ella se describe como con las variables descritas anteriormente, se puede padecer o no de un accidente cerebro vascular.
Mediante un sistema de puntaje meticulosamente diseñado por la NINDS.
    
Probabilidad en 10 años >= 88%
puntos >= 30
"""


def preprocess():
    global diseases_list, diseases_symptoms, symptom_map, d_desc_map, d_treatment_map
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, "diseases.txt")
    diseases = open(file_path, encoding="utf-8")
    diseases_t = diseases.read()
    diseases_list = diseases_t.split("\n")
    diseases.close()
    for disease in diseases_list:
        disease_s_file = open(
            module_dir + "/Disease symptoms/" + disease + ".txt", encoding="utf-8"
        )
        disease_s_data = disease_s_file.read()
        s_list = disease_s_data.split("\n")
        diseases_symptoms.append(s_list)
        symptom_map[str(s_list)] = disease
        disease_s_file.close()
        disease_s_file = open(
            module_dir + "/Disease descriptions/" + disease + ".txt", encoding="utf-8"
        )
        disease_s_data = disease_s_file.read()
        d_desc_map[disease] = disease_s_data
        disease_s_file.close()
        disease_s_file = open(
            module_dir + "/Disease treatments/" + disease + ".txt", encoding="utf-8"
        )
        disease_s_data = disease_s_file.read()
        d_treatment_map[disease] = disease_s_data
        disease_s_file.close()


def get_details(disease):
    return d_desc_map[disease]


def get_treatments(disease):
    return d_treatment_map[disease]


def if_not_matched(disease):
    global id_disease_response, description_response, treatment_response
    print("")
    id_disease = disease
    disease_details = get_details(id_disease)
    treatments = get_treatments(id_disease)

    id_disease_response = disease
    description_response = get_details(id_disease)
    treatment_response = get_treatments(id_disease)

    print("")
    print("The most probable disease that you have is %s\n" % id_disease)
    print("A short description of the disease is given below :\n")
    print(disease_details + "\n")
    print(
        "The common medications and procedures suggested by other real doctors are: \n"
    )
    print(treatments + "\n")


class Greetings(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        print("")
        print("Hi! I am Dr.Yar, I am here to help you make your health better.")
        print("For that you'll have to answer a few questions about your conditions")
        print("Do you feel any of the following symptoms:")
        print("")
        yield Fact(action="find_disease")

    @Rule(Fact(action="find_disease"), NOT(Fact(gender=W())), salience=1)
    def symptom_0(self):
        self.declare(Fact(gender=var1))

    @Rule(Fact(action="find_disease"), NOT(Fact(age=W())), salience=1)
    def symptom_1(self):
        self.declare(Fact(age=var2))

    @Rule(Fact(action="find_disease"), NOT(Fact(pas_no_trat=W())), salience=1)
    def symptom_2(self):
        self.declare(Fact(pas_no_trat=var3))

    @Rule(Fact(action="find_disease"), NOT(Fact(pas_trat=W())), salience=1)
    def symptom_3(self):
        self.declare(Fact(pas_trat=var4))

    @Rule(Fact(action="find_disease"), NOT(Fact(diabetes=W())), salience=1)
    def symptom_4(self):
        self.declare(Fact(diabetes=var5))

    @Rule(Fact(action="find_disease"), NOT(Fact(smoking_status=W())), salience=1)
    def symptom_5(self):
        self.declare(Fact(smoking_status=var6))

    @Rule(Fact(action="find_disease"), NOT(Fact(ecv=W())), salience=1)
    def symptom_6(self):
        self.declare(Fact(ecv=var7))

    @Rule(Fact(action="find_disease"), NOT(Fact(fa=W())), salience=1)
    def symptom_7(self):
        self.declare(Fact(fa=var8))

    @Rule(Fact(action="find_disease"), NOT(Fact(hvi=W())), salience=1)
    def symptom_8(self):
        self.declare(Fact(hvi=var9))

    @Rule(
        Fact(action="find_disease"),
        AND(
            Fact(gender="yes"),
            Fact(age="yes"),
            Fact(pas_no_trat="yes"),
            Fact(pas_trat="yes"),
            Fact(diabetes="yes"),
            Fact(smoking_status="yes"),
            Fact(ecv="yes"),
            Fact(fa="yes"),
            Fact(hvi="yes"),
        ),
    )
    def disease_0(self):
        self.declare(Fact(disease="ataque-cerebrovascular"))

    @Rule(
        Fact(action="find_disease"),
        AND(
            Fact(gender="no"),
            Fact(age="no"),
            Fact(pas_no_trat="no"),
            Fact(pas_trat="no"),
            Fact(diabetes="no"),
            Fact(smoking_status="no"),
            Fact(ecv="no"),
            Fact(fa="no"),
            Fact(hvi="no"),
        ),
    )
    def disease_1(self):
        self.declare(Fact(disease="no-ataque-cerebrovascular"))

    @Rule(Fact(action="find_disease"), Fact(disease=MATCH.disease), salience=-998)
    def disease(self, disease):
        global id_disease_response, description_response, treatment_response
        print("")
        id_disease = disease
        disease_details = get_details(id_disease)
        treatments = get_treatments(id_disease)

        id_disease_response = disease
        description_response = get_details(id_disease)
        treatment_response = get_treatments(id_disease)

        print("")
        print("The most probable disease that you have is %s\n" % id_disease)
        print("A short description of the disease is given below :\n")
        print(disease_details + "\n")
        print(
            "The common medications and procedures suggested by other real doctors are: \n"
        )
        print(treatments + "\n")

    @Rule(
        Fact(action="find_disease"),
        Fact(gender=MATCH.gender),
        Fact(age=MATCH.age),
        Fact(pas_no_trat=MATCH.pas_no_trat),
        Fact(pas_trat=MATCH.pas_trat),
        Fact(diabetes=MATCH.diabetes),
        Fact(smoking_status=MATCH.smoking_status),
        Fact(ecv=MATCH.ecv),
        Fact(fa=MATCH.fa),
        Fact(hvi=MATCH.hvi),
        NOT(Fact(disease=MATCH.disease)),
        salience=-999,
    )
    def not_matched(
        self, gender, age, pas_no_trat, pas_trat, diabetes, smoking_status, ecv, fa, hvi
    ):
        lis = [
            gender,
            age,
            pas_no_trat,
            pas_trat,
            diabetes,
            smoking_status,
            ecv,
            fa,
            hvi,
        ]
        print(
            "<----------->" + gender,
            age,
            pas_no_trat,
            pas_trat,
            diabetes,
            smoking_status,
            ecv,
            fa,
            hvi,
        )
        max_count = 0
        max_disease = ""
        for key, val in symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if temp_list[j] == lis[j] and lis[j] == "no":
                    count = count + 1
            if count > max_count:
                max_count = count
                max_disease = val
        if_not_matched(max_disease)


def make_engine():
    engine = Greetings()
    engine.reset()  # Prepare the engine for the execution.
    engine.run()  # Run it!
