import unittest
import requests
import json 

class Numbers(unittest.TestCase):

    def test_api_get1(self):
        cevap = requests.get("https://automationexercise.com/api/productsList")
        print (cevap.text)

    def test_api_post(self):
        payload = {"key1":"value1"}
        gonder = requests.post("https://automationexercise.com/api/productsList", data=payload)
        print(gonder.status_code)

    def test_api_get2(self):
        payload = {"key1":"value1"}
        cevap = requests.post("https://automationexercise.com/api/brandsList", data=payload)
        print (cevap.text)
        print (cevap.status_code)

    def test_api_get3(self):
        cevap = requests.get("https://automationexercise.com/api/brandsList")
        icerik = json.loads(cevap.text)
        item_id = icerik["brands"][1]["id"]
        self.assertEqual(2, item_id)

    def test_api_put(self):
        api_url = "https://automationexercise.com/api/brandsList"
        request_data = {"search_product":"top"}
        response = requests.put(api_url, data=request_data)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        content = json.loads(response.text)
        

    def test_api_post3(self):
        api_url = "https://automationexercise.com/api/searchProduct"
        request_data = {"search_product": "top"}
        response = requests.post(api_url, data=request_data)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        content = json.loads(response.text)
        self.assertEqual("Tops", content["products"][0]["category"]["category"])

    def test_api_post4(self):
        api_url = "https://automationexercise.com/api/verifyLogin"
        request_data = {"email": "uguremirsay@gmail.com"}  
        response = requests.post(api_url, data=request_data)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        print("Response Message:", response.text)

    def test_api_delete(self):
        api_url = "https://automationexercise.com/api/verifyLogin"
        request_data = {"email": "uguremirsay@gmail.com"} 
        response = requests.delete(api_url, data=request_data)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        print("Response Message:", response.text)


    def test_api_create_account_test_post_6(self):
        api_url = "https://automationexercise.com/api/createAccount"
        request_data = {
            "name": "Ugur Say",
            "email": "uguremirsaygmail.com",
            "password": "secure_password",
            "title": "Mr",
            "birth_date": "00",
            "birth_month": "00",
            "birth_year": "2000",
            "firstname": "Ugur",
            "lastname": "Say",
            "company": "Amazon",
            "address1": "Mehmetcik",
            "address2": "Denizkent",
            "country": "Turkey",
            "zipcode": "34520",
            "state": "Beylikduzu",
            "city": "Istanbul",
            "mobile_number": "5452064456"
        }
        response = requests.post(api_url, data=request_data)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        print("Response Message:", response.text)

    def test_api_delete2(self):
        api_url = "https://automationexercise.com/api/deleteAccount"
        request_data = {"email": "uguremirsay@mail.com" , 'password':'12345'} 
        response = requests.delete(api_url, data=request_data)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        print("Response Message:", response.text)

    def test_api_delete3(self):
        api_url = "https://automationexercise.com/api/deleteAccount"
        request_data = {"email": "uguremirsay@gmail.com" , 'password':'12345'} 
        response = requests.delete(api_url, data=request_data)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        print("Response Message:", response.text)

    def test_api_put2(self):
        api_url = "https://automationexercise.com/api/updateAccount"
        request_data = {
            "name": "Ugur Say",
            "email": "uguremirsay@gmail.com",
            "password": "secure_password",
            "title": "Mr",
            "birth_date": "00",
            "birth_month": "00",
            "birth_year": "2000",
            "firstname": "Ugur",
            "lastname": "Say",
            "company": "Amazon",
            "address1": "Mehmetcik",
            "address2": "Denizkent",
            "country": "Turkey",
            "zipcode": "34520",
            "state": "Beylikduzu",
            "city": "Istanbul",
            "mobile_number": "5452064456"
        } 
        response = requests.put(api_url, data=request_data)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        print("Response Message:", response.text)

    def test_api_get4(self):
        api_url = "https://automationexercise.com/api/getUserDetailByEmail"
        request_data = {"email": "uguremirsay@gmail.com"} 
        response = requests.delete(api_url, data=request_data)
        self.assertEqual(response.status_code, 200, "Expected status code 200")
        print("Response Message:", response.text)

if __name__ == '__main__':
    unittest.main()