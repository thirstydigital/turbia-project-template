from django.test import TestCase, TransactionTestCase
from django_webtest import WebTest
from {{ project_name }} import forms
from {{ project_name }} import models
from {{ project_name }} import views

class Forms(WebTest):
	def test(self):
		pass

class Models(WebTest):
	def test(self):
		pass

class Views(WebTest):
	def test(self):
		pass
