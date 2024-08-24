from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import (Product, 
                    ProductMen,
                    ProductFeminine,
                    ProductChildish, 
                    ProductWashing, 
                    ProductOffice, 
                    ProductCooking,
                    ProductHeadphone,
                    ProductLaptop,
                    ProductRefriGerator,
                    ProductListblog,
                    )


class TestProduct(TestCase):
    
    def setUp(cls):

        cls.product1 = Product.objects.create(
            title='product1',
            description='this is car',
            price='360000',
            
            
          
        )
        cls.product2 = ProductMen.objects.create(
            title='product2',
            description='this is car',
            price='360000',
            
            
        )
        cls.product3 = ProductFeminine.objects.create(
            title='product3',
            description='this is car',
            price='360000',
            
            
        )
        cls.product4 = ProductChildish.objects.create(
            title='product4',
            description='this is car',
            price='360000',
            
            
        )
        cls.product5 = ProductWashing.objects.create(
            title='product5',
            description='this is car',
            price='360000',
            
            
        )
        cls.product6 = ProductOffice.objects.create(
            title='product6',
            description='this is car',
            price='360000',
            
            
        )
        cls.product7 = ProductCooking.objects.create(
            title='product7',
            description='this is car',
            price='360000',
            
            
        )
        cls.product8 = ProductHeadphone.objects.create(
            title='product8',
            description='this is car',
            price='360000',
            
            
        )
        cls.product9 = ProductLaptop.objects.create(
            title='product9',
            description='this is car',
            price='360000',
            
            
        )
        cls.product10 = ProductRefriGerator.objects.create(
            title='product10',
            description='this is car',
            price='360000',
            
            
        )
        cls.product11 = ProductListblog.objects.create(
            title='product11',
            description='this is car',
            
            
        )





    def test_product1_model_str(self):
        product = self.product1
        self.assertEqual(str(product), product.title)

    def test_product_detail(self):
        self.assertEqual(self.product1.title, 'product1')
        self.assertEqual(self.product1.description, 'this is car')
        self.assertEqual(self.product1.price, '360000')  
       
    def test_product_list_url(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_product_list_url_by_name(self):
        response = self.client.get(reverse('product_list')) 
        self.assertEqual(response.status_code, 200)

    def test_product_title_on_page_list(self):
        response = self.client.get(reverse('product_list'))
        self.assertContains(response, self.product1.title)
      
    def test_product_template_name(self):  
        response = self.client.get(reverse("product_list"))
        self.assertTemplateUsed(response, "products/product_list.html")  
    
    def test_product2_model_str(self):
        product = self.product2
        self.assertEqual(str(product), product.title)

    def test_product_detail_men(self):
        self.assertEqual(self.product2.title, 'product2')
        self.assertEqual(self.product2.description, 'this is car')
        self.assertEqual(self.product2.price, '360000')  
           

    def test_product_men_list_url(self):
        response = self.client.get('/products/men/')
        self.assertEqual(response.status_code, 200)

    
    def test_product_men_list_url_by_name(self):
        response = self.client.get(reverse('product_list_men')) 
        self.assertEqual(response.status_code, 200)    

    
    def test_product_title_men_on_page_list(self):
        response = self.client.get(reverse('product_list_men'))
        self.assertContains(response, self.product2.title)
          
    def test_product_men_template_name(self):  
        response = self.client.get(reverse("product_list_men"))
        self.assertTemplateUsed(response, "products/product_list_men.html")        

    def test_product3_model_str(self):
        product = self.product3
        self.assertEqual(str(product), product.title)

    def test_product_detail_feminine(self):
        self.assertEqual(self.product3.title, 'product3')
        self.assertEqual(self.product3.description, 'this is car')
        self.assertEqual(self.product3.price, '360000')  
           

    def test_product_feminine_list_url(self):
        response = self.client.get('/products/feminine/')
        self.assertEqual(response.status_code, 200)

    
    def test_product_feminine_list_url_by_name(self):
        response = self.client.get(reverse('product_list_feminine')) 
        self.assertEqual(response.status_code, 200)    

    
    def test_product_title_feminine_on_page_list(self):
        response = self.client.get(reverse('product_list_feminine'))
        self.assertContains(response, self.product3.title)
          
    def test_product_feminine_template_name(self):  
        response = self.client.get(reverse("product_list_feminine"))
        self.assertTemplateUsed(response, "products/product_list_feminine.html")             

    
    def test_product4_model_str(self):
        product = self.product4
        self.assertEqual(str(product), product.title)

    def test_product_detail_childish(self):
        self.assertEqual(self.product4.title, 'product4')
        self.assertEqual(self.product4.description, 'this is car')
        self.assertEqual(self.product4.price, '360000')  
           

    def test_product_childish_list_url(self):
        response = self.client.get('/products/childish/')
        self.assertEqual(response.status_code, 200)

    
    def test_product_childish_list_url_by_name(self):
        response = self.client.get(reverse('product_list_childish')) 
        self.assertEqual(response.status_code, 200)    

    
    def test_product_title_childish_on_page_list(self):
        response = self.client.get(reverse('product_list_childish'))
        self.assertContains(response, self.product4.title)
          
    def test_product_childish_template_name(self):  
        response = self.client.get(reverse("product_list_childish"))
        self.assertTemplateUsed(response, "products/product_list_childish.html")                 
    
    def test_product5_model_str(self):
        product = self.product5
        self.assertEqual(str(product), product.title)

    def test_product_detail_washing(self):
        self.assertEqual(self.product5.title, 'product5')
        self.assertEqual(self.product5.description, 'this is car')
        self.assertEqual(self.product5.price, '360000')  
           

    def test_product_washing_list_url(self):
        response = self.client.get('/products/washing/')
        self.assertEqual(response.status_code, 200)

    
    def test_product_washing_list_url_by_name(self):
        response = self.client.get(reverse('product_list_washing')) 
        self.assertEqual(response.status_code, 200)    

    
    def test_product_title_washing_on_page_list(self):
        response = self.client.get(reverse('product_list_washing'))
        self.assertContains(response, self.product5.title)
          
    def test_product_washing_template_name(self):  
        response = self.client.get(reverse("product_list_washing"))
        self.assertTemplateUsed(response, "products/product_list_washing machine.html")      

    def test_product6_model_str(self):
        product = self.product6
        self.assertEqual(str(product), product.title)

    def test_product_detail_office(self):
        self.assertEqual(self.product6.title, 'product6')
        self.assertEqual(self.product6.description, 'this is car')
        self.assertEqual(self.product6.price, '360000')  
           

    def test_product_office_list_url(self):
        response = self.client.get('/products/office/')
        self.assertEqual(response.status_code, 200)

    
    def test_product_office_list_url_by_name(self):
        response = self.client.get(reverse('product_list_office')) 
        self.assertEqual(response.status_code, 200)    

    
    def test_product_title_office_on_page_list(self):
        response = self.client.get(reverse('product_list_office'))
        self.assertContains(response, self.product6.title)
          
    def test_product_office_template_name(self):  
        response = self.client.get(reverse("product_list_office"))
        self.assertTemplateUsed(response, "products/product_list_office.html")        

    
    def test_product7_model_str(self):
        product = self.product7
        self.assertEqual(str(product), product.title)

    def test_product_detail_cooking(self):
        self.assertEqual(self.product7.title, 'product7')
        self.assertEqual(self.product7.description, 'this is car')
        self.assertEqual(self.product7.price, '360000')  
           

    def test_product_cooking_list_url(self):
        response = self.client.get('/products/cooking/')
        self.assertEqual(response.status_code, 200)

    
    def test_product_cooking_list_url_by_name(self):
        response = self.client.get(reverse('product_list_cooking')) 
        self.assertEqual(response.status_code, 200)    

    
    def test_product_title_cooking_on_page_list(self):
        response = self.client.get(reverse('product_list_cooking'))
        self.assertContains(response, self.product7.title)
          
    def test_product_cooking_template_name(self):  
        response = self.client.get(reverse("product_list_cooking"))
        self.assertTemplateUsed(response, "products/product_list_cooking.html")       
     
    def test_product8_model_str(self):
        product = self.product8
        self.assertEqual(str(product), product.title)

    def test_product_detail_headphone(self):
        self.assertEqual(self.product8.title, 'product8')
        self.assertEqual(self.product8.description, 'this is car')
        self.assertEqual(self.product8.price, '360000')  
           

    def test_product_headphone_list_url(self):
        response = self.client.get('/products/headphone/')
        self.assertEqual(response.status_code, 200)

    
    def test_product_headphone_list_url_by_name(self):
        response = self.client.get(reverse('product_list_headphone')) 
        self.assertEqual(response.status_code, 200)    

    
    def test_product_title_headphone_on_page_list(self):
        response = self.client.get(reverse('product_list_headphone'))
        self.assertContains(response, self.product8.title)
          
    def test_product_headphone_template_name(self):  
        response = self.client.get(reverse("product_list_headphone"))
        self.assertTemplateUsed(response, "products/product_list_headphone.html")   

    
    def test_product9_model_str(self):
        product = self.product9
        self.assertEqual(str(product), product.title)

    def test_product_detail_laptop(self):
        self.assertEqual(self.product9.title, 'product9')
        self.assertEqual(self.product9.description, 'this is car')
        self.assertEqual(self.product9.price, '360000')  
           

    def test_product_laptop_list_url(self):
        response = self.client.get('/products/laptop/')
        self.assertEqual(response.status_code, 200)

    
    def test_product_laptop_list_url_by_name(self):
        response = self.client.get(reverse('product_list_laptop')) 
        self.assertEqual(response.status_code, 200)    

    
    def test_product_title_laptop_on_page_list(self):
        response = self.client.get(reverse('product_list_laptop'))
        self.assertContains(response, self.product9.title)
          
    def test_product_laptop_template_name(self):  
        response = self.client.get(reverse("product_list_laptop"))
        self.assertTemplateUsed(response, "products/product_list_laptop.html")      

    
    def test_product10_model_str(self):
        product = self.product10
        self.assertEqual(str(product), product.title)

    def test_product_detail_laptop(self):
        self.assertEqual(self.product10.title, 'product10')
        self.assertEqual(self.product10.description, 'this is car')
        self.assertEqual(self.product10.price, '360000')  
           

    def test_product_refrigerator_list_url(self):
        response = self.client.get('/products/refrigerator/')
        self.assertEqual(response.status_code, 200)

    
    def test_product_refrigerator_list_url_by_name(self):
        response = self.client.get(reverse('product_list_refrigerator')) 
        self.assertEqual(response.status_code, 200)    

    
    def test_product_title_refrigerator_on_page_list(self):
        response = self.client.get(reverse('product_list_refrigerator'))
        self.assertContains(response, self.product10.title)
          
    def test_product_refrigerator_template_name(self):  
        response = self.client.get(reverse("product_list_refrigerator"))
        self.assertTemplateUsed(response, "products/product_list_Refrigerator.html")        

    def test_product11_model_str(self):
        product = self.product11
        self.assertEqual(str(product), product.title)

    def test_product_detail_blog(self):
        self.assertEqual(self.product11.title, 'product11')
        self.assertEqual(self.product11.description, 'this is car')
           

    def test_product_blog_list_url(self):
        response = self.client.get('/products/blog/')
        self.assertEqual(response.status_code, 200)

    
    def test_product_blog_list_url_by_name(self):
        response = self.client.get(reverse('product_list_blog')) 
        self.assertEqual(response.status_code, 200)    

    
    def test_product_title_blog_on_page_list(self):
        response = self.client.get(reverse('product_list_blog'))
        self.assertContains(response, self.product11.title)
          
    def test_product_blog_template_name(self): 
        response = self.client.get(reverse("product_list_blog"))
        self.assertTemplateUsed(response, "products/product_list_blog.html")   

    def test_product_men_detail_view_status_code(self):
         response = self.client.post(reverse('product_detail_men', args=[self.product2.id]))
         self.assertEqual(response.status_code, 405)
    
    def test_product_feminine_detail_view_status_code(self):
         response = self.client.post(reverse('product_detail_feminine', args=[self.product3.id]))
         self.assertEqual(response.status_code, 405)
    
    def test_product_childish_detail_view_status_code(self):
         response = self.client.post(reverse('product_detail_childish', args=[self.product4.id]))
         self.assertEqual(response.status_code, 405)

    def test_product_washing_detail_view_status_code(self):
         response = self.client.post(reverse('product_detail_washing', args=[self.product5.id]))
         self.assertEqual(response.status_code, 405)

    def test_product_office_detail_view_status_code(self):
         response = self.client.post(reverse('product_detail_office', args=[self.product6.id]))
         self.assertEqual(response.status_code, 405)

    def test_product_cooking_detail_view_status_code(self):
         response = self.client.post(reverse('product_detail_cooking', args=[self.product7.id]))
         self.assertEqual(response.status_code, 405)               

    def test_product_headphone_detail_view_status_code(self):
         response = self.client.post(reverse('product_detail_headphone', args=[self.product8.id]))
         self.assertEqual(response.status_code, 405)     

    def test_product_laptop_detail_view_status_code(self):
         response = self.client.post(reverse('product_detail_laptop', args=[self.product9.id]))
         self.assertEqual(response.status_code, 405)     

    def test_product_refrigerator_detail_view_status_code(self):
         response = self.client.post(reverse('product_detail_refrigerator', args=[self.product10.id]))
         self.assertEqual(response.status_code, 405)     

    def test_product_blog_detail_view_status_code(self):
         response = self.client.post(reverse('product_detail_blog', args=[self.product11.id]))
         self.assertEqual(response.status_code, 405)                                   