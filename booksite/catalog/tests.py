from django.test import TestCase
import unittest
from .models import Publisher,Title
from django.db import IntegrityError
from django.test import Client

class DatabaseTests(unittest.TestCase):
	'''check cannot create two different publishers with the same value of the pub_id field'''
	def test_primary_key(self):
		All_table=Publisher.objects.all()
		All_table.delete()
		Create_pub=Publisher.objects.create(pub_id=877,pub_name='Binnet & Hardley',city='Boston')
		def throwException(value):
			try:
				compare_pub=Publisher.objects.create(pub_id=value,pub_name='Binnet & Hard',city='Boston')
			except IntegrityError:
				print 'UNIQUE constraint failed: catalog_publisher.pub_id'
		self.assertRaises(IntegrityError,throwException(877))
		
	'''check publisher name must be unique'''	
	def test_unique_name(self):
		All_table=Publisher.objects.all()
		All_table.delete()
		Create_pub=Publisher.objects.create(pub_id=877,pub_name='Binnet & Hardley',city='Boston')
		def throwException(value):
			try:
				compare_pub=Publisher.objects.create(pub_id=867,pub_name=value,city='Boston')
			except IntegrityError:
				print 'UNIQUE constraint failed: catalog_publisher.pub_name'
		self.assertRaises(IntegrityError,throwException('Binnet & Hardley'))
		
	'''confirm a title will be saved properly if all values are valid'''
	def test_title_validInput(self):
		All_table=Publisher.objects.all().delete()
		Create_pub=Publisher.objects.create(pub_id=877,pub_name='Binnet & Hardley',city='Boston')
		Delte_all_table=Title.objects.all().delete()
		try:
			Compare_title=Title.objects.create(title_id='MC2222',title='Silicon Valley Gastronomto Treats',category='mod_cook',price=19.99,pub_id=Create_pub)
		except ValueError:
			print 'Value Error Not pass'
			self.assertTrue(False)
		#print 'pass'

	'''check cannot create two different titles with the same value of the title_id field'''
	def test_same_title_id(self):
		Delte_all_table=Publisher.objects.all().delete()
		Create_pub=Publisher.objects.create(pub_id=877,pub_name='Binnet & Hardley',city='Boston')
		try:
			Compare_title1=Title.objects.create(title_id='MC2222',title='Silicon Valley Gastronomto Treats',category='mod_cook',price=19.99,pub_id=Create_pub)
		except ValueError:
			print 'Value Error Not pass'
			self.assertTrue(False)
		try:
			Compare_title2=Title.objects.create(title_id='MC2222',title='Net Etiquette',category='business',price=19.99,pub_id=Create_pub)
		except IntegrityError:
			print 'IntegrityError: UNIQUE constraint failed: catalog_title.title_id'
			self.assertTrue(True)

	'''confirm cannot create a title without a publisher'''
	def test_create_title_without_publisher(self):
		All_table=Publisher.objects.all().delete()
		Delte_all_table=Title.objects.all().delete()
		#print n	
		try:
			T=Title.objects.create(title_id='MC2222',title='Net Etiquette',category='business',price=19.99)
		except IntegrityError:
			print 'IntegrityError: NOT NULL constraint failed: catalog_title.pub_id_id'
			self.assertTrue(True)


class ViewTest(unittest.TestCase):
	'''check http://127.0.0.1:8000/catalog/ can run perfectly or not'''
	def test_index_view(self):
		client=Client()
		response=client.get('/catalog/')
		#print response.content
		self.assertEqual(response.status_code,200)
		#print 'pass'
	
	'''check http://127.0.0.1:8000/catalog/add/publisher/ could run and check if it can add publisher into database or not'''
	def test_add_publisher_view(self):
		client=Client()
		response=client.post('/catalog/add/publisher/',{'pub_id': 736,'pub_name':'New Moon Books','city':'Boston'})
		#print response.content+'hahaah'
		self.assertEqual(response.status_code,302)
		All_table=Publisher.objects
		#print All_table.all()
		find_table=All_table.filter(pub_name='New Moon Books')
		#print find_table 
		self.assertEqual(str(find_table),"[<Publisher: New Moon Books>]")
	
	'''check http://127.0.0.1:8000/catalog/add/title could run and could add title into database correctly or not'''
	def test_add_title_view(self):
		client=Client()
		response=client.post('/catalog/add/title/',{'title_id': 'BU2075','title':'You Can Combat computer stress!','category':'business','price':'2.99','pub_id':'736'})
		
		self.assertEqual(response.status_code,302)
		find_table=Title.objects.filter(title='You Can Combat computer stress!')
		#print find_table
		self.assertEqual(str(find_table),"[<Title: You Can Combat computer stress!>]")
	
	'''check http://127.0.0.1:8000/catalog/get/titles/by/publisher could run and the when give correct pub_name, it will return the correct information related to publisher'''
	def test_get_title_by_publisher_view(self):
		client=Client()
		response=client.post('/catalog/get/titles/by/publisher/',{'publisher':'New Moon Books'})
		self.assertEqual(response.status_code,200)
		#print response.content
		self.assertIn('You Can Combat computer stress! 2.99',response.content)
	
	'''test http://127.0.0.1:8000/catalog/get/publisher/of/title could run and test given a correct title and return correct infomation '''
	def test_find_publisher_of_title_view(self):
		client=Client()
		response=client.post('/catalog/get/publisher/of/title/',{'title':'You Can Combat computer stress!'})
		#print response.status_code
		self.assertEqual(response.status_code,200)
		self.assertIn('The publisher is New Moon Books',response.content)

suite =unittest.TestLoader().loadTestsFromTestCase(DatabaseTests)
unittest.TextTestRunner(verbosity=2).run(suite)

suite =unittest.TestLoader().loadTestsFromTestCase(ViewTest)
unittest.TextTestRunner(verbosity=2).run(suite)
