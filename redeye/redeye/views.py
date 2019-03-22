from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from crowdfunder.models import Project, RewardTier, Purchase
from crowdfunder.forms import RewardTierForm, PurchaseForm, ProjectForm, LoginForm
import ipdb
import datetime
