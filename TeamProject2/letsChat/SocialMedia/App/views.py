
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.http import JsonResponse
import random
from django.core.mail import send_mail
from .models import *
from django.contrib.auth.hashers import make_password,check_password
import time
import datetime
import uuid,json
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models import Q
# from django.core import serializers
from itertools import chain
from django.urls import reverse
# from django_pandas.io import read_frame
from django.db.models import Subquery

import pickle

@csrf_exempt
def update_session(request):
	if not request.is_ajax() or not request.method=='POST':
		return HttpResponseNotAllowed(['POST'])
	userRegistration.objects.filter(userId=request.session['user']).update(is_online=True)
	return HttpResponse(request.session['user'])

	# if request.POST.get('action') == 'offline':
	# 	# userId = request.session['user']
	# 	userRegistration.objects.filter(userId=request.session['user']).update(is_online=False)
	# 	return HttpResponse(request.session['user'])

def index(request):
	if request.session.has_key('user'):
		userInfo = userRegistration.objects.get(userId=request.session['user'])
		userData = UserPost.objects.filter(userId=request.session['user']).order_by('-date') # '-' for descending order
		
		friends = AllFriends.objects.get(userId=request.session['user']).Friends
		
		postList = []
		def UserAllPost():
			for item in userData:
				yield item

		def FriendPosts():
			for friend in friends:
				friendPost = UserPost.objects.filter(userId=friend).order_by('-date')
				for post in friendPost:
					yield post
		# FriendPosts()
		storyList = []
		StoryOwnerList = []
		tempStoryList = []
		tempStoryOwner = ""
		tempMedia = ""
		tempUploadTime = ""
		tempStoryType = ""
		tempFontFamily = ""
		tempFontSize = ""
		tempCaption = ""
		tempColor = ""
		lenthCaption = ""
		#Check myself Stories
		myStories = Story.objects.filter(userId=request.session['user'])
		if myStories.exists():
			StoryOwner = userRegistration.objects.get(userId=request.session['user'])
			for l in myStories:
				lenthCaption =lenthCaption + str(len(l.Caption)) +"@"
				tempMedia = tempMedia + "/media/"+str(l.media) +"@"
				tempUploadTime = tempUploadTime + str(l.uploadTime) +"@"
				tempStoryType = tempStoryType + l.storyType +"@"
				tempFontFamily = tempFontFamily + l.fontFamily +"@"
				tempFontSize = tempFontSize + l.fontSize +"@"
				tempCaption = tempCaption + l.Caption 
				tempColor = tempColor + l.color +"@"
				
				tempStoryOwner = "Me" + ","
				StoryOwner.userName = " Me"
			StoryOwnerList.append(StoryOwner)
			tempStoryList.insert(0,tempMedia)
			tempStoryList.insert(1,tempUploadTime)
			tempStoryList.insert(2,tempStoryType)
			tempStoryList.insert(3,tempFontFamily)
			tempStoryList.insert(4,tempFontSize)
			tempStoryList.insert(5,tempCaption)
			tempStoryList.insert(6,tempColor)
			tempStoryList.insert(7,lenthCaption)		
			
			storyList.append(tempStoryList)
			
			
		#Get Friends Sttories
		for friend in friends:
			#print(friend)
			allStories = Story.objects.filter(userId=friend)
			#print(allStories)
			if allStories.exists():
				StoryOwner = userRegistration.objects.get(userId=friend)
				print(len(allStories))
				tempStoryList = []
				tempStoryOwner = ""
				tempMedia = ""
				tempUploadTime = ""
				tempStoryType = ""
				tempFontFamily = ""
				tempFontSize = ""
				tempCaption = ""
				tempColor = ""
				lenthCaption = ""
				for l in allStories:
					lenthCaption =lenthCaption + str(len(l.Caption)) +"@"
					tempMedia = tempMedia + "/media/"+str(l.media) +"@"
					tempUploadTime = tempUploadTime + str(l.uploadTime) +"@"
					tempStoryType = tempStoryType + l.storyType +"@"
					tempFontFamily = tempFontFamily + l.fontFamily +"@"
					tempFontSize = tempFontSize + l.fontSize +"@"
					tempCaption = tempCaption + l.Caption 
					tempColor = tempColor + l.color +"@"
					
				StoryOwnerList.append(StoryOwner)
				tempStoryList.insert(0,tempMedia)
				tempStoryList.insert(1,tempUploadTime)
				tempStoryList.insert(2,tempStoryType)
				tempStoryList.insert(3,tempFontFamily)
				tempStoryList.insert(4,tempFontSize)
				tempStoryList.insert(5,tempCaption)
				tempStoryList.insert(6,tempColor)
				tempStoryList.insert(7,lenthCaption)		
				
				storyList.append(tempStoryList)
					#storyList.append(l)	
					#StoryOwnerList.append(StoryOwner)

		storiesFullData = zip(StoryOwnerList,storyList)
		AllPost = chain(UserAllPost(), FriendPosts())
		for item in AllPost:
			postList.append(item)
		postList.sort(key=lambda x: x.date,reverse = True) 
		like=[]; colorPost = []
		for i in postList:
			likes = Likes.objects.get(postId=i.postId)
			like.append(len(likes.postLikedBy))
			if request.session['user'] in likes.postLikedBy:
				colorPost.append("rgba(0, 150, 136,1)")
			else:
				colorPost.append("grey")

		qry =[]
		lnth = []
		for item in postList:
			poId=item.postId
			try:
				s =(TaggedPeople.objects.get(postId=poId).taggedPersons)
				qry.append(userRegistration.objects.filter(userId=s[0]))
				lnth.append(len(s)-1)
			except:
				qry.append("")
				lnth.append("")

		commentContent = []
		commentName = []
		commentPic = []
		commentId = []
		for i in postList:
			commentData = []
			commentData.append(Comments.objects.filter(postId=i.postId).order_by('-date'))
			for j in commentData:
				print("j value = ",j)
				if j:
					for k in j:
						commentContent.append(k.comment)
						commentName.append(k.userInfo.firstName + ' ' + k.userInfo.lastName)
						commentPic.append(k.userInfo.profilePic)
						commentId.append(k.commentId)
				else:
					commentContent.append("")
					commentName.append("")
					commentPic.append("")
					commentId.append("")
					 	
				break

		notification = Notifications.objects.filter(receiver=request.session['user']).order_by('-date')
		totalNotification = notification.filter(viewed=False).count()
		picsList1 = []
		uname = ''   # IF USER HAS NO NOTIFICATION
		for Id in notification:
			senderDetail = userRegistration.objects.filter(userId=Id.sender)
			for detail in senderDetail:
				
				uname = detail.userName
				picUrl = detail.profilePic
				picsList1.append(picUrl.url)
		params = {'userInfo':userInfo,'userData':zip(postList, like,colorPost,qry,lnth,commentContent,commentName,commentPic,commentId),'date_now':datetime.datetime.now(),
		'allComments':zip(postList),"storyData":storiesFullData,'notification':zip(notification,picsList1),
		'totalNotification':totalNotification}
		return render(request,'ds.html',params)
	else:
		return render(request,'index.html')

def signup(request):
	if request.method == "POST":
		fName = request.POST.get('firstName').title()
		lName = request.POST.get('lastName').title()
		username = request.POST.get('userName')
		email = request.POST.get('Email')
		otp = request.POST.get('OneTimePass')
		pwd = request.POST.get('Password')
		mobile = request.POST.get('Mobile')
		
		if((otp == request.session["Otp"])):
			if userRegistration.objects.filter(emailAddress=email):
				return render(request,'CreateAccount.html',{'message':'Account Already Present with Given Email'})
			elif userRegistration.objects.filter(mobile=mobile):
				return render(request,'CreateAccount.html',{'message':'Account Already Present with Given Mobile Number'}) 
			else:
				userRegistration(userId=username, firstName=fName, lastName=lName, userName=username, 
				mobile=mobile,emailAddress = email, password = make_password(pwd)).save()
				# Creating Blank Frined List
				AllFriends(userId=username).save()
				code = str(username + "profile").encode('utf-8')
				createAlbum(userId = username,albumName="profile",albumId=code.hex()).save()
				
				code = str(username + "cover").encode('utf-8')
				createAlbum(userId = username,albumName="cover",albumId=code.hex()).save()
				return HttpResponseRedirect('/')	
		else:
			return render(request,'CreateAccount.html',{'message':'Incorrect OTP'})
	else:
		return render(request,'CreateAccount.html')

@csrf_exempt
def OtpGeneration(request):
	Email=request.POST.get('Email','DefaultValue')
	RandomValue="LetsChat"+str(random.randint(1001,99999))
	print(RandomValue)
	request.session["Otp"]=RandomValue
	message=f"Your Email Address  {Email}  Your OTP is {RandomValue} Do not share your password to anyone."
	send_mail(
    	'LetsChat',
    	message,
    	settings.EMAIL_HOST_USER,
    	[Email],
    	fail_silently=False)
	request.session["Otp"]=RandomValue
	request.session["Email"]=Email
	return JsonResponse({'Result':"Successfully"})

def login(request):
	if request.method == 'POST':
		email = request.POST.get("login_Email")
		password = request.POST.get("password")
		loginValidate = userRegistration.objects.get(emailAddress=email)
		encryptPass = loginValidate.password

		if check_password(password,encryptPass) == True:
			request.session['user'] = str(loginValidate.userId)
			# name = request.session['user']
			request.session['name'] = str(loginValidate.firstName) + ' ' + str(loginValidate.lastName)
			request.session['pic'] = str(loginValidate.profilePic) # THIS LINE IS CURRENTLY NOT IN USE 
			return HttpResponseRedirect('/')
		else:
			return render(request,'index.html',{'message':'Please Check Your Email and Password'})
	else:
		if request.session.has_key('user'):
			return HttpResponseRedirect('/')
		else:
			return render(request,'index.html')

def logout(request):
	if request.session.has_key('user'):
		del request.session['user']
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')

def search(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			query = request.POST.get('search').title()
			userProfile = userRegistration.objects.filter(firstName=query) | userRegistration.objects.filter(lastName=query)
			if userProfile:
				params = {'Users':userProfile,'name':request.session['user']}
				return render(request,'Search.html',params)
			else:
				return HttpResponse('No user')
		else:
			return HttpResponse('No POST method')
	else:
		return HttpResponse("/")

@csrf_exempt
def uservalidate(request):
	username = request.POST.get('username')
	if userRegistration.objects.filter(userName=username):
		return JsonResponse({'Result':1})
	else:
		return JsonResponse({'Result':0})	

def imageStory(request):
	if request.session.has_key('user'):
		return render(request,'imageStory.html')
	else:
		return HttpResponseRedirect("/")

def textStory(request):
	if request.session.has_key('user'):
		return render(request,'textStory.html')
	return HttpResponseRedirect("/")

def imageStorySubmissionForm(request):
	if request.session.has_key('user'):
		if request.method == 'POST':
			image = request.FILES.get('image')
			print(image)
			fontSize = request.POST.get('fontSize',"defaultValue")
			storyType = request.POST.get('type',"defaultValue")
			fontFamily = request.POST.get('fontFamily',"defaultValue")
			Caption = request.POST.get('Caption',"defaultValue")
			color = request.POST.get('color',"defaultValue")
			
			Story(userId=request.session['user'],media=image,storyType=storyType,fontFamily=fontFamily,fontSize=fontSize,Caption=Caption,color=color).save()
			return HttpResponseRedirect("/")
		else:
			stories = Story.objects.all()
			return JsonResponse({"Status":"UnSuccessfully"})
	else:
		return HttpResponseRedirect("/")

@csrf_exempt
def story(request):
	if request.session.has_key('user'):
		print('here in stort')
		if request.method == 'POST':
			image = request.FILES.get('image')
			print(image)
			fontSize = request.POST.get('fontSize',"defaultValue")
			storyType = request.POST.get('type',"defaultValue")
			fontFamily = request.POST.get('fontFamily',"defaultValue")
			Caption = request.POST.get('Caption',"defaultValue")
			color = request.POST.get('color',"defaultValue")
			
			Story(userId=request.session['user'],media=image,storyType=storyType,fontFamily=fontFamily,fontSize=fontSize,Caption=Caption,color=color).save()
			return JsonResponse({"Status":"Successfully"})
		else:
			stories = Story.objects.all()
			return JsonResponse({"Status":"UnSuccessfully"})
	else:
		return HttpResponseRedirect("/")

@csrf_exempt
def storydelete(request):
	if request.session.has_key('user'):
		from datetime import timedelta 
		
		tm1 = (datetime.datetime.now() - timedelta(minutes=1))
		
		s = Story.objects.filter(uploadTime__lte= tm1).delete()
		
		return JsonResponse({'Result':'Deleted'})
	else:
		return HttpResponseRedirect("/")

def PostSubmission(request):
	if request.session.has_key('user'):
		postType = 'post'
		Id = uuid.uuid4().hex	
		user = request.session['user']
		PostMessage = request.POST.get('Post_Title','DefaultValue')
		PostMedia = request.FILES.get('MediaFile')
	
		PostStatus = UserPost(PostType=postType,postId=Id,userId=user,userName=request.session['name'],post=PostMedia,
		Message = PostMessage,userPic='/media/'+str(userRegistration.objects.get(userId=user).profilePic)
		).save()
		tagging = TaggedPeople(taggedId=request.session['name']+Id,postId=Id).save()
		likes = Likes(postId=Id).save()
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')
	# return render(request,'DashBoard.Html',{"flag":"Your post has uploaded"})

@csrf_exempt
def postlike(request):
	if request.session.has_key('user'):
		postId = request.POST.get('postId')
		postLikedOf = request.POST.get('postLikedOf')
		postLiker = request.POST.get('postLikedBy')

		likes = Likes.objects.get(postId=postId)
		if postLiker in likes.postLikedBy: # Checking if friend has already liked 
			likes.postLikedBy.remove(postLiker)
			LikesList = likes.postLikedBy
			Likes.objects.filter(postId=postId).update(postId=postId,postLikedBy=LikesList)
			totalLikes = len(LikesList)

			Notifications.objects.filter(postId=postId,notificationType='like',sender=postLiker).delete()
			return JsonResponse({'Result':'Success','totalLikes':totalLikes,'message':'unliked'})

		else:
			likes.postLikedBy.append(postLiker)
			LikesList = likes.postLikedBy
			Likes.objects.filter(postId=postId).update(postId=postId,postLikedBy=LikesList)
			totalLikes = len(LikesList)

			if postLikedOf != postLiker:
				postLikedByPerson = userRegistration.objects.get(userId=postLiker)
				postLikedByPersonName = str(postLikedByPerson.firstName) + ' ' + str(postLikedByPerson.lastName)
				notificationMessage = postLikedByPersonName + ' Liked your Post'
				Notifications(postId=postId,notificationType='like',fullName=postLikedByPersonName,sender=postLiker,
					receiver=postLikedOf,notification=notificationMessage,viewed=False).save()
			return JsonResponse({'Result':'Success','totalLikes':totalLikes,'message':'liked'})
	else:
		return HttpResponseRedirect("/")
	
@csrf_exempt
def postcomment(request):
	if request.session.has_key('user'):
		commentedBy = request.POST.get('postCommentedBy')

		commenter = userRegistration.objects.get(userId=commentedBy)
		if request.POST.get('action'):
			return JsonResponse({'Result':'Success','commenter':str(commenter),'pic':str(commenter.profilePic.url)})

		postId = request.POST.get('postId')
		commentedOf = request.POST.get('postCommentedOf')
		comment = request.POST.get('comment')
		commentId = 'comment'+str(uuid.uuid4().hex)
		name = userRegistration.objects.get(userId=commentedBy)
		fullname = commenter.firstName + ' ' + commenter.lastName
		notify = fullname + ' commented on your post'

		Comments(postId=postId,commentedOf=commentedOf,commentedBy=commentedBy,comment=comment,commentId=commentId,
		userInfo=name).save()

		Notifications(postId=postId,notificationType='comment',fullName=name,sender=commentedBy,receiver=commentedOf,
		notification=notify,viewed=False).save()
		return JsonResponse({'Result':'Success','comment':comment})
	return HttpResponseRedirect("/")

@csrf_exempt
def reply(request):
	if request.session.has_key('user'):
		postId = request.POST.get('postId')
		commentId = request.POST.get('commentId')
		replyId = 'reply'+str(uuid.uuid4().hex)
		repliedBy = request.POST.get('repliedBy')
		repliedOn = request.POST.get('repliedOn')
		reply = request.POST.get('reply')
		user = userRegistration.objects.get(userId=repliedBy)
		print(user)
		
		Replies(postId=postId,commentId=commentId,replyId=replyId,repliedBy=repliedBy,repliedOn=repliedOn,reply=reply,
		userInfo=user).save()
		
		notify = str(user) + ' Replied to your Comment'
		Notifications(postId=postId,notificationType='reply',fullName=str(user),sender=repliedBy,receiver=repliedOn,
		notification=notify,viewed=False).save()
		return JsonResponse({'Success':'Done'})
	else:
		return HttpResponseRedirect("/")

def reportGetPost(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			pic = request.POST.get('pic',"defaultValue")
			msg = request.POST.get('msg',"defaultValue")
			postId = request.POST.get('postId',"defaultValue")
			if(pic=="defaultValue"):
				pic=False
			print(postId)
			param={"pic":pic,"msg":msg,"postId":postId}
			return render(request,'report.html',param)
		else:
			return HttpResponseRedirect("/")

@csrf_exempt
def reportSubmission(request):
	if request.session.has_key('user'):		
		if request.method == "POST":
			postId = request.POST.get("postID")
			reportTitle = request.POST.get("reportTitle")
			print(postId)
			Report(postId=postId,reportTitle=reportTitle).save()
			return JsonResponse({"status":True})
	else:
		return HttpResponseRedirect("/")

@csrf_exempt
def taggedSearchFriends(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			if request.POST.get('action') == 'friend':
				friend = request.POST.get('id')
				friends = AllFriends.objects.get(userId=friend).Friends	
				username = []
				pic = []
				userId = []
				for i in friends:
					userId.append(i)
					friendName = userRegistration.objects.get(userId=i)
					username.append(friendName.firstName + ' ' +friendName.lastName)
					pic.append(friendName.profilePic.url)
					
				return JsonResponse({"name":username,"pic":pic,'userId':userId})
			elif request.POST.get('action') == 'groupCreationListfriend':
				friends = AllFriends.objects.get(userId=request.session['user']).Friends
				personName = []
				personPic = []
				username = []
				for item in friends:
					print(item)
					userFrnd = userRegistration.objects.get(userId = item)
					personName.append(userFrnd.firstName+" "+ userFrnd.lastName)
					personPic.append((userFrnd.profilePic).url)
					username.append(userFrnd.userId)
				return JsonResponse({'name':personName,'pic':personPic,'userId':username})
			elif request.POST.get('action') == 'groupUpdationListfriend':
				friends = AllFriends.objects.get(userId=request.session['user']).Friends
				personName = []
				personPic = []
				username = []
				for item in friends:
					userFrnd = userRegistration.objects.get(userId = item)
					personName.append(userFrnd.firstName+" "+ userFrnd.lastName)
					personPic.append((userFrnd.profilePic).url)
					username.append(userFrnd.userId)
				qry5=Groups.objects.get(groupId=request.POST.get('group')).Members
				qry10=Groups.objects.get(groupId=request.POST.get('group'))

				return JsonResponse({'name':personName,'pic':personPic,'userId':username,'member':qry5,'groupName':qry10.groupName,'groupDescription':qry10.groupInfo,'groupPic':qry10.groupPic.url})

			else:
				friends = AllFriends.objects.get(userId=request.session['user']).Friends
				pid = request.POST.get('postId')
				tagPerson = TaggedPeople.objects.filter(postId=pid)
				for person in tagPerson:
					tagPersonList = person.taggedPersons
				else:
					tagPersonList = []
				taggedUsers = [userRegistration.objects.filter(userId=user) for user in tagPersonList]
				allName = []
				for userQuerySet in taggedUsers:
					for user in userQuerySet:
						fname = user.firstName
						lname = user.lastName
						allName.append(fname+' '+lname)
				username = []
				pic = []
				userId = []
				for i in friends:
					userId.append(i)
					friendName = userRegistration.objects.get(userId=i)
					username.append(friendName.firstName + ' ' +friendName.lastName)
					pic.append(friendName.profilePic.url)
					
				return JsonResponse({"name":username,"pic":pic,'userId':userId,'allTaggedList':tagPersonList,'allName':allName})
	else:
		return HttpResponseRedirect("/")	

@csrf_exempt
def tagSubmissionForm(request):
	if request.session.has_key('user'):
		tagPerson = request.POST.get('tagPerson')
		postId = request.POST.get('postId')
		tagPersonList = list(tagPerson.split(","))
		taggedBy = request.session['user']
		taggedByPerson = userRegistration.objects.get(userId=taggedBy)
		notify = "You and "  +str(int(len(tagPersonList))-2)+ " others are tagged in " + str(taggedByPerson)+ "\'s post"
		TaggedPeople.objects.filter(postId=postId).update(taggedPersons=tagPerson[1:])
		print(notify)
		for taggedUser in tagPersonList:
			if taggedUser == '':
				pass
			else:
				name = userRegistration.objects.get(userId=str(taggedUser))
				Notifications(postId=postId,notificationType='tag',fullName=str(taggedByPerson),sender=taggedBy,receiver=taggedUser,
				notification=notify,viewed=False).save()
		return HttpResponse(tagPerson) 
	return HttpResponseRedirect("/")

@csrf_exempt
def showAllTagPerson(request):
	if request.session.has_key('user'):
		postId = request.POST.get('postId')
		qry = TaggedPeople.objects.get(postId = postId).taggedPersons
		Fname =[]
		Lname =[] 
		for person in qry:
			qry1=userRegistration.objects.get(userName=person)
			Fname.append(qry1.firstName)
			Lname.append(qry1.lastName)

		return JsonResponse({"status":"successfully","userName":qry,"FName":Fname,"LName":Lname})
	return HttpResponseRedirect("/")

@csrf_exempt
def CommentShow(request):
	if request.session.has_key('user'):
		ParentcommentByList = []
		ParentComment = []
		parentcommentName = []
		ParentcommentId = []
		ParentcommentUserpic = []
		childComment=[]
		childCommentBy = []
		childcommentId=[]
		childcommentName=[]
		childcommentUserpic = []
		comments = Comments.objects.filter(postId=request.POST.get("postId"))
		for comment in comments:
			ParentcommentByList.append(comment.commentedBy)
			ParentComment.append(comment.comment)
			ParentcommentId.append(comment.commentId)
			parentcommentName.append(comment.userInfo.firstName +' '+ comment.userInfo.lastName)
			ParentcommentUserpic.append(comment.userInfo.profilePic.url)
			childComments = Replies.objects.filter(commentId=comment.commentId)
			for child in childComments:
				childCommentBy.append(child.repliedBy)
				childComment.append(child.reply)
				childcommentId.append(child.commentId)
				childcommentName.append(child.userInfo.firstName +' '+ child.userInfo.lastName)
				childcommentUserpic.append(child.userInfo.profilePic.url)
		return JsonResponse({"ParentcommentByList":ParentcommentByList,"ParentComment":ParentComment,"ParentcommentId":ParentcommentId,"parentcommentName":
		parentcommentName,"childcommentId":childcommentId,"ChildComment":childComment,"childcommentName":childcommentName,
		"childCommentBy":childCommentBy,"ParentcommentUserpic":ParentcommentUserpic,"childcommentUserpic":childcommentUserpic})
	else:
		return HttpResponseRedirect("/")

def changepassword(request):
	if request.session.has_key('user'):
		if request.method == 'POST':
			currentPass = request.POST.get('currentPass')
			newPass = request.POST.get('newPass')
			confirmPass = request.POST.get('confirmPass')
			if newPass != confirmPass:
				message = "Password Do not match"
				return render(request,'changepwd.html',{'message':message})
			else:
				encryptCurrentPass = userRegistration.objects.get(userId=request.session['user']).password

				if check_password(currentPass,encryptCurrentPass) == True:
					userRegistration.objects.filter(userId=request.session['user']).update(password=make_password(newPass))
					# return render(request,'changepwd.html',{'message':'Password Changed Successfully.Please Login Again'})
					
					del request.session['user']
					return HttpResponseRedirect('/')
				else:
					return HttpResponse('pasword not match')
		else:
			return render(request,'changepwd.html')
	else:
		return HttpResponseRedirect("/")

#Forget Password
def forgetPassword(request):
	return render(request,'forgetPassword.html')

@csrf_exempt 
def forgetPasswordOTP(request):
	Email=request.POST.get("Email",'DefaultValue')
	print(Email)
	if request.method == "POST" and Email!="DefaultValue" and Email!="":
		RandomValue=random.randint(1001,99999)
		RandomValue="LetsChat"+str(RandomValue)
		print(RandomValue)
		message=f"Your Email Address  {Email}  Your OTP is {RandomValue} for Forget Password Do not share your password to anyone."
		send_mail(
	    	'LetsChat', 
	    	message,
	    	settings.EMAIL_HOST_USER,
	    	[Email],
	    	fail_silently=False)
		request.session["forgetOtp"]=RandomValue
		return JsonResponse({'Result':"Successfully"})
	else:
		return JsonResponse({'Result':"UnSuccessfully"})

#Forget Password Process
@csrf_exempt
def forgetPasswordProcess(request):
	if request.method == "POST":
		OTP = request.POST.get('Otp','DefaultValue')
		Email = request.POST.get('userName','DefaultValue')
		if(request.session["forgetOtp"]==OTP):
			print("OTP MATCH")
			return render(request,'forgetPasswordProcess.html',{"Email":Email})
		else:
			return HttpResponse("<center><h1>Your Password is Incorrect<h1><center>")
	return HttpResponseRedirect("/")


@csrf_exempt
def changeForgetPasword(request):
	if request.method == "POST":
		Email = request.POST.get('Email','DefaultValue')
		fPassword = request.POST.get('fPassword','DefaultValue')
		sPassword = request.POST.get('sPassword','DefaultValue')
		if fPassword == sPassword:
			#print("SuccessFully")
			del request.session['forgetOtp']
			userRegistration.objects.filter(emailAddress=Email).update(password=make_password(fPassword))
			#print(Email)
			#Clear all Exist Session for Logout Devices
			if request.session.has_key('user'):
				del request.session['user']
				del request.session['name']
				del request.session['pic']
			return JsonResponse({"Status":"Successfully"})
		else:
			#print("UnSuccessFully")
			return JsonResponse({"Status":"UnSuccessfully"})
	else:
		return HttpResponseRedirect("/")


def album(request):
	if request.session.has_key('user'):
		photos = UserPost.objects.filter(userId=request.session['user'])
		myGallery = createAlbum.objects.filter(userId=request.session['user'])
		code = str(request.session['user'] + "profile").encode('utf-8')
		code = code.hex()
		profileData = AlbumImageData.objects.filter(albumId = code)
		# profiledataList = []
		# for item in profileData:
		# 	profiledataList.append(item.media.url)
		code = str(request.session['user'] + "cover").encode('utf-8')
		code = code.hex()
		coverData = AlbumImageData.objects.filter(albumId = code)
		# coverdataList = []
		# for item in coverData:
		# 	profiledataList.append(item.media.url)
		print(myGallery)
		print("photos = ",photos)
		

		params = {'photos':photos,'myGallery':myGallery,'profileData':profileData,'coverData':coverData}
		return render(request,'Album.html',params)
	else:
		return HttpResponseRedirect('/')

# def createAlbumDetails

def searchProfile(request):
	if request.session.has_key('user'):
		profile = request.POST.get('profile')
		username = userRegistration.objects.get(userId=profile).userName
		return HttpResponseRedirect('/profile/'+username+'/')
	else:
		return HttpResponseRedirect("/")

def profile(request,user):
	if request.session.has_key('user'):
		ActiveUser = userRegistration.objects.get(userId=request.session['user'])
		ActiveUserName = ActiveUser.firstName
		ActiveUserPic = ActiveUser.profilePic

		profileId = user
		profileDetail = userRegistration.objects.get(userId=user)
		userPic = profileDetail.profilePic

		if Friend_Requests.objects.filter(receiver=profileId,sender=request.session['user']):
			isRequest = True
			isRequested = False

		elif Friend_Requests.objects.filter(receiver=request.session['user'],sender=profileId):
			isRequested = True
			isRequest = False
		else:
			isRequest = False
			isRequested = False

		# Extracting friend list of searched user
		friends = AllFriends.objects.get(userId=request.session['user']).Friends
		# Logic for setting button of Add Friend, Unfriend
		if profileId in friends:
			isFriend = True
		else:
			isFriend = False

		request.session['Watchprofile'] = profileId
		postList = []
		postData = UserPost.objects.filter(userId=user).order_by('-date')
		like=[]; colorPost = []
		for post in postData:
			postList.append(post)
		for post in postList:
			likes = Likes.objects.get(postId=post.postId)
			like.append(len(likes.postLikedBy))
			if request.session['user'] in likes.postLikedBy:
					colorPost.append("rgba(0, 150, 136,1)")
			else:
				colorPost.append("grey")
		 
		
		params = {'data':profileDetail,'currentUserId':request.session['user'],'currentUserFullName':request.session['name'],
			'currentUserPic':userPic.url,'isFriend':isFriend,'isRequest':isRequest,'isRequested':isRequested,'ActiveUserPic':ActiveUserPic,'ActiveUser':ActiveUser.userName
		,'ActiveUserName':ActiveUserName,'postData':zip(postData, like,colorPost)}
		return render(request,'Profile1.html',params)
	else:
		return HttpResponseRedirect("/")

def myfriends(request):
	if request.session.has_key('user'):
		friends = AllFriends.objects.get(userId=request.session['user']).Friends
		friendList = []
		for friend in friends:
			friendData = userRegistration.objects.filter(userId=friend)
			friendList.append(friendData)

		
		params = {'friendList':friendList}
		return render(request,'MyFriends.html',params)
	else:
		return HttpResponseRedirect("/")

@csrf_exempt
def myFriendsProcess(request):
	if request.session.has_key('user'):
		if request.method == 'POST':
			sortBY=request.POST.get("sortBy",'DefaultValue')
			lt = []
			friendList = AllFriends.objects.get(userId=request.session['user']).Friends
			for name in friendList:
				lt.append(userRegistration.objects.get(userId=name))
			firstName=[]
			lastName=[]
			prfilePic=[]
			Id=[]
			quote=[]
			sortList = []
			if sortBY=="firstName":
				for j in lt:
					sortList.append(j)
					sortList.sort(key=lambda x: x.firstName)
			else :
				for j in lt:
					sortList.append(j)
					sortList.sort(key=lambda x: x.lastName)
			for j in sortList:
				firstName.append(j.firstName)
				lastName.append(j.lastName)
				prfilePic.append(j.profilePic.url)
				Id.append(j.userId)
				quote.append(j.quote)
			return JsonResponse({"FName":firstName,"lName":lastName,"pPic":prfilePic,"EmailId":Id,"quote":quote})
		else :
			return HttpResponse("<center><h1>You did something wrong</h1></center>")
	else:
		return HttpResponseRedirect("/")

@csrf_exempt
def addfriend(request):
	if request.session.has_key('user'):
		profileId = request.POST.get('profileId')
		action = request.POST.get('action')
		print(action)
		request.session['friendProfile'] = profileId # USED IN NEXT FUNCTION FOR REQUEST CONFIRM

		if action == 'add':
			sendRequest = Friend_Requests(sender=request.session['user'],receiver=profileId,senderName=request.session['name'])
			sendRequest.save()
			return JsonResponse({"Result":"Successfully Sent"})

		elif action == 'cancel':
			Friend_Requests.objects.filter(sender=request.session['user'],receiver=profileId).delete()
			return JsonResponse({"Result":"Successfully Canceled"})
		
		elif action == 'unfriend':
			friend = AllFriends.objects.get(userId=request.session['user'])
			friend.Friends.remove(profileId)
			friendList = friend.Friends
			AllFriends.objects.filter(userId=request.session['user']).update(userId=request.session['user'],Friends=friendList)
			
			friend1 = AllFriends.objects.get(userId=profileId)
			friend1.Friends.remove(request.session['user'])
			friendList1 = friend1.Friends
			AllFriends.objects.filter(userId=profileId).update(userId=profileId,Friends=friendList1)
	# Deleting Notifications 
			Notifications.objects.filter(notificationType='friend',sender=request.session['user'],receiver=profileId).delete()
			Notifications.objects.filter(notificationType='friend',sender=profileId,receiver=request.session['user']).delete()
			return JsonResponse({"Result":"Successfully Removed"})

		elif action == 'confirm':
			print('views conf')
			return HttpResponseRedirect('/requestConfirm')
		
		elif action == 'changeRequestHTML':
			return JsonResponse({"Result":"Successfully Removed"})

		elif action == 'changeNotificationHTML':
			senderDetail = userRegistration.objects.get(userId=profileId)
			senderName = str(senderDetail.firstName) + ' ' + str(senderDetail.lastName)
			senderPic = str(senderDetail.profilePic.url)
			return JsonResponse({"Result":"Successfully Removed","name":senderName,"pic":senderPic})
		
		elif action == 'changeDashboardHTML':
			return JsonResponse({"Result":"Successfully Removed"})	
		else:
			return JsonResponse({'Result':'Nothing Done'})
	else:
		return HttpResponseRedirect("/")

@csrf_exempt
def requestConfirm(request):
	if request.session.has_key('user'):
		if request.method == 'POST':
			friendId = request.POST.get('sender')
			myId = request.session['user']
			action = request.POST.get('action')
		
		else:
			# myId = 'mohammad.danish2694@gmail.com'
			# friendId = 'sj27754@gmail.com'
			# action = 1
			friendId = request.session['friendProfile'] # GETTING VALUE FROM PREVIOUS FUNCTION ADD FRIEND
			myId = request.session['user']
			
			action = 'add'
		if action == 'add':
			# Friend Add in Logged user List
			myList = AllFriends.objects.get(userId=myId)
			if friendId in myList.Friends: # Checking if friend is already added 
				pass
			else:
				myList.Friends.append(friendId)
				myNewList = myList.Friends
				AllFriends.objects.filter(userId=myId).update(userId=myId,Friends=myNewList)

			# Friend Add in Sender user List
			friendList = AllFriends.objects.get(userId=friendId)
			if myId in friendList.Friends: # Checking if friend is already added 
				pass
			else:
				friendList.Friends.append(myId)
				friendNewList = friendList.Friends
				AllFriends.objects.filter(userId=friendId).update(userId=friendId,Friends=friendNewList)
			
			senderName = Friend_Requests.objects.get(sender=friendId).senderName
		notify = request.session['name'] + ' accepted your Friend Request.'

		Notifications(notificationType='friend',sender=myId,receiver=friendId,fullName=request.session['name'],
		notification=notify,viewed=False).save()

		Friend_Requests.objects.filter(sender=friendId,receiver=myId).delete()
		senderPic = userRegistration.objects.get(userId=myId).profilePic
		return JsonResponse({'Result':'Succuss','name':senderName,'receiver':friendId,'senderPic':senderPic.url})
	else:
		return HttpResponseRedirect("/")


@csrf_exempt
def notifications(request):
	if request.session.has_key('user'):
		if request.POST.get('action'):
			print('viewd')
			Notifications.objects.filter(receiver=request.session['user'],viewed=False).update(viewed=True)
			return JsonResponse({'Success':'Success'})
		else:
			# IT IS INCOMPLETE ONLY DIPLAYS FRIEND REQUESTS AND ACCEPT NOTIFICATIONS
			fRequests = Friend_Requests.objects.filter(receiver=request.session['user']).order_by('-date')
			picsList = []
			for Id in fRequests:
				senderPic = userRegistration.objects.filter(userId=Id.sender)
				for pic in senderPic:
					picUrl = pic.profilePic
					picsList.append(picUrl.url)
			
			notification = Notifications.objects.filter(receiver=request.session['user']).order_by('-date')
			picsList1 = []
			uname = ''   # IF USER HAS NO NOTIFICATION
			for Id in notification:
				senderDetail = userRegistration.objects.filter(userId=Id.sender)
				for detail in senderDetail:
					
					uname = detail.userName
					picUrl = detail.profilePic
					picsList1.append(picUrl.url)

			params = {'request':zip(fRequests,picsList),'notification':zip(notification,picsList1),'UserName':uname,'userProfile':request.session['user']}
			return render(request,'Notifications.html',params)
	else:
		return HttpResponseRedirect("/")

@csrf_exempt
def liveSearchProcess(request):
	from django.core import serializers
	from django.http import JsonResponse
	if request.method == "POST":
		name=request.POST.get('search','DefaultValue')
		liveResult = userRegistration.objects.filter(Q(firstName__icontains=name) | Q(lastName__icontains=name))
		print(liveResult)
		name=[]
		pic=[]
		uId=[]
		uname = []
		for e in liveResult:
			fullName = e.firstName+ ' ' +e.lastName
			name.append(fullName)
			uId.append(e.userId)
			pic.append(e.profilePic.url)
			uname.append(e.userName)
		# print(pic)
		return JsonResponse({"Username":name,"Id":uId,"picture":pic,"uname":uname})

def userProfileInsert(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			profileUserId=request.POST.get('ProfileUser')
			profileImage=request.FILES['profileImage']
			loginUser=request.session['user']
			postType = 'profilePhoto'
			Id = uuid.uuid4().hex	
			user = request.session['user']
			PostMessage = ''
		
			if profileUserId==loginUser:
				status=userRegistration.objects.get(userId=loginUser)
				status.profilePic = profileImage
				status.save()
				UserPost.objects.filter(userId=loginUser).update(userPic='/media/'+str(userRegistration.objects.get(userId=loginUser).profilePic))
				GroupChat.objects.filter(sender=loginUser).update(senderPic='/media/'+str(userRegistration.objects.get(userId=loginUser).profilePic))
				# if not Album.objects.filter(AlbumID=request.session['user']):
					# Album(AlbumID=request.session['user'],Name='Profile Pictures').save()
				
				PostStatus = UserPost(PostType=postType,postId=Id,userId=user,userName=request.session['name'],post=profileImage,
				Message = PostMessage,userPic='/media/'+str(userRegistration.objects.get(userId=user).profilePic)
				).save()
				likes = Likes(postId=Id).save()
				# Photos(Album='Profile Pictures',PhotoID=request.session['user'],Image=profileImage).save()


				code = str(request.session['user'] + "profile").encode('utf-8')
				img = []
				picId = []
				t = time.localtime()
				current_time = time.strftime("%H:%M:%S", t)	
				current_time =(str(current_time).encode('utf-8')).hex()+code.hex() 
				
				AlbumImageData(albumId=code.hex(),media=profileImage,picAlbumId=current_time).save()

				return HttpResponseRedirect('/profile/'+loginUser+'/')
			else:
				return HttpResponse('<center><h1>you did somethong wrong</h1></center>')
		else:
			return HttpResponse('<center><h1>you did somethong wrong</h1></center>')
	else:
		return HttpResponseRedirect("/")

@csrf_exempt
def userIntroInsert(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			print("request.session['Watchprofile']",request.session['Watchprofile'])
			v1 = request.session['Watchprofile']
			v2 = request.session['user']
			if  v1 == v2:
				quote = request.POST.get('quote','DefaultValue')

				dOB = request.POST.get('dOB','DefaultValue')
				if dOB == "DefaultValue":
					dOB=""
				print(dOB)
				gender = request.POST.get('gender','DefaultValue')
				if(gender == "Gender"):
					gender = ""
				mobileNumber = request.POST.get('mobileNumber','DefaultValue')
				countryName = request.POST.get('countryName','DefaultValue')
				cityName = request.POST.get('cityName','DefaultValue')
				currentEducation = request.POST.get('currentEducation','DefaultValue')
				educationStartYear = request.POST.get('educationStartYear','DefaultValue')
				educationEndYear = request.POST.get('educationEndYear','DefaultValue')
				companyName = request.POST.get('companyName','DefaultValue')
				companyPosition = request.POST.get('companyPosition','DefaultValue')
				companyCity = request.POST.get('companyCity','DefaultValue')
				companyDescription = request.POST.get('companyDescription','DefaultValue')
				status=userRegistration.objects.filter(userId=v2).update(quote=quote,dOB=dOB,gender=gender,mobile=mobileNumber,countryName=countryName,
				cityName=cityName,currentEducation=currentEducation,educationStartYear=educationStartYear,educationEndYear=educationEndYear,companyName=companyName,companyPosition=companyPosition,companyCity=companyCity,companyDescription=companyDescription)

				return JsonResponse({"status":"success"})
			else:
				return JsonResponse({"status":"Unsuccess"})
	else:
		return HttpResponseRedirect("/")

def userCoverInsert(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			profileUserId = request.POST.get('coverUser','DefaultValue')
			coverImage = request.FILES['coverImage']
			loginUser = request.session['user']
			postType = 'coverPhoto'
			Id = uuid.uuid4().hex	
			user = request.session['user']
			PostMessage = ''
			if profileUserId==loginUser:
				status = userRegistration.objects.get(userId=loginUser)
				status.coverPic = coverImage
				status.save()
				# if not Album.objects.filter(AlbumID=request.session['user'],Name='Cover Photos'):
					# Album(AlbumID=request.session['user'],Name='Cover Photos').save()
				
				PostStatus = UserPost(PostType=postType,postId=Id,userId=user,userName=request.session['name'],post=coverImage,
				Message = PostMessage,userPic='/media/'+str(userRegistration.objects.get(userId=user).profilePic)
				).save()
				likes = Likes(postId=Id).save()
				Photos(Album='Cover Photos',PhotoID=request.session['user'],Image=coverImage).save()

				code = str(request.session['user'] + "cover").encode('utf-8')
				img = []
				picId = []
				t = time.localtime()
				current_time = time.strftime("%H:%M:%S", t)	
				current_time =(str(current_time).encode('utf-8')).hex()+code.hex() 
				
				AlbumImageData(albumId=code.hex(),media=coverImage,picAlbumId=current_time).save()
				return HttpResponseRedirect('/profile/'+loginUser+'/')
			else:
				return HttpResponse('<center><h1>you did somethong wrong</h1></center>')
		else:
			return HttpResponse('<center><h1>you did somethong wrong</h1></center>')
	else:
		return HttpResponseRedirect("/")

def friendSearch(request):
	if request.session.has_key('user'):
		return render(request,'Friends.html')
	else:
		return HttpResponseRedirect("/")

@csrf_exempt
def outgoingRequest(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			liveResult = Friend_Requests.objects.filter(sender=request.session['user'])
			reciverId=[]
			reciverPic=[]
			receiverName=[]
			

			for e in liveResult:
				reciverId.append(e.receiver)
				userQry=userRegistration.objects.get(userId=e.receiver)
				receiverName.append(userQry.firstName +" "+userQry.lastName)
				reciverPic.append(userQry.profilePic.url)
			return JsonResponse({"reciverId":reciverId,'receiverName':receiverName,'reciverPic':reciverPic})
	else: 
		return HttpResponseRedirect("/")

@csrf_exempt
def incomingRequest(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			liveResult = Friend_Requests.objects.filter(receiver=request.session['user'])
			senderName=[]
			senderId=[]
			senderPic=[]
			
			for e in liveResult:
				senderName.append(e.senderName)
				senderId.append(e.sender)
				senderQry=userQry=userRegistration.objects.get(userId=e.sender)
				senderPic.append(senderQry.profilePic.url)
			return JsonResponse({"senderName":senderName,"senderId":senderId,'pic':senderPic})
	else:
		return HttpResponseRedirect("/")

def test(request):
	userId = 'danish26'
	Friend = 'shubham31'
	# m = GroupChat.objects.values_list('Members', flat=True)
	g = userRegistration.objects.get(userId=request.session['user']).Groups
	print(g)	
	return JsonResponse({'Result':'Success'})
	# Likes(postId = 'cd2d8468aa37496899616e746f30be4b').save()
	# return render(request,'test.html')


def friends(request):
	if request.session.has_key('user'):
		friendList = []; MessageList = []
		friends = AllFriends.objects.get(userId=request.session['user']).Friends
		
		for friend in friends:
			friendData = userRegistration.objects.filter(userId=friend)
			unreadMessage = Messages.objects.filter(is_read=False,sender=friend,receiver=request.session['user']).count()
			MessageList.append(unreadMessage)
			friendList.append(friendData)

		friendMessageList = zip(friendList,MessageList)
		GroupsList = []; GroupsMsgList = []
		groups = userRegistration.objects.get(userId=request.session['user']).Groups
		for group in groups:
			allGroups = Groups.objects.filter(groupId=group)
			unreadMessage = GroupChat.objects.filter(is_read=False).exclude(sender=request.session['user']).count()
			GroupsList.append(allGroups)
			GroupsMsgList.append(unreadMessage)
		groupMessageList = zip(GroupsList,GroupsMsgList)
		return friendMessageList,groupMessageList
	else:
		return HttpResponseRedirect("/")

def messages(request):
	if request.session.has_key('user'):
		friendList,GroupsList = friends(request)
		myData = userRegistration.objects.get(userId=request.session['user'])
		params = {'friendList':friendList,'myData':myData,'groups':GroupsList}
		return render(request,'chat.html',params)
	else:
		return HttpResponseRedirect("/")

def inbox(request,user):
	if request.session.has_key('user'):
		myId = request.session['user']
		friendId = user
		is_Inbox = Inbox.objects.filter(Users=[myId,friendId]) | Inbox.objects.filter(Users=[friendId,myId])
		seenMessage(request,user,request.session['user'])
		if is_Inbox:
			for msg in is_Inbox:
				inboxId = msg.inboxId
				messageInbox = msg.id
			allMessages = Messages.objects.filter(Inbox=messageInbox)
			unread = allMessages.filter(is_read=False,sender=user).count()
			print(unread)
		else:
			inboxId = uuid.uuid4().hex
			Inbox(inboxId=inboxId,Users=[myId,friendId]).save()
			allMessages = ''
		myData = userRegistration.objects.get(userId=request.session['user'])
		friendData = userRegistration.objects.get(userId = user)
		friendList,groups = friends(request)

		return render(request,'chat.html',{"inbox":True,"friendData":friendData,'inboxId':inboxId,
			'myData':myData,'allMessages':allMessages,'friendList':friendList,'groups':groups})
	else:
		return HttpResponseRedirect("/")	
def groups(request,group):
	if request.session.has_key('user'):
		myId = request.session['user']
		allMessages = GroupChat.objects.filter(groupId=group)
		
		myData = userRegistration.objects.get(userId=request.session['user'])
		# GroupChat.objects.filter(is_read=False).exclude(sender=request.session['user']).update(is_read=True)
		friendList,groups = friends(request)
		groupInfo = Groups.objects.get(groupId=group)

		gpPersonId = []
		gpPersonName = []
		gpPersonPic = []
		groupRights=False
		if request.session['user'] == groupInfo.Members[-1]:
			groupRights = True

		for item in groupInfo.Members:
			groupCandidateData = userRegistration.objects.get(userId = item)
			gpPersonId.append(item)
			gpPersonName.append(groupCandidateData.firstName+" "+groupCandidateData.lastName)
			gpPersonPic.append(groupCandidateData.profilePic.url)

		return render(request,'chat.html',{"groupChat":True,'groupId':group,'myData':myData,
			'friendList':friendList,'groups':groups,'allMessages':allMessages,'groupInfo':groupInfo,
			'gpPerson':zip(gpPersonName,gpPersonId,gpPersonPic),"groupRights":groupRights})
	return HttpResponseRedirect("/")

@csrf_exempt
def saveMessage(request):
	if request.session.has_key('user'):
		inboxId = request.POST.get('inboxId')
		messageid = 'privatemessage'+str(uuid.uuid4())
		sender = request.POST.get('sender')
		receiver = request.POST.get('receiver')
		message = request.POST.get('Message')

		Messages(Inbox=Inbox.objects.get(inboxId=inboxId),MessageID=messageid,sender=sender,
		receiver=receiver,is_read=False,Message=message).save()
		return JsonResponse({'Result':'Success'})
	else:
		return HttpResponseRedirect("/")

@csrf_exempt
def groupMessage_Save(request):
	if request.session.has_key('user'):
		groupId = request.POST.get('groupId')
		sender = request.POST.get('sender')
		message = request.POST.get('Message')
		messageid = 'groupmessage'+str(uuid.uuid4())

		senderDetail = userRegistration.objects.get(userId=sender)
		GroupChat(groupId=groupId,messageID=messageid,sender=sender,is_read=False,Message=message,
		senderName=senderDetail.firstName+' '+senderDetail.lastName,senderPic='/media/'+str(senderDetail.profilePic),
		Group=Groups.objects.get(groupId=groupId)).save()
		return JsonResponse({'Result':'Success'})
	else:
		return HttpResponseRedirect("/")

@csrf_exempt
def seenMessage(request,sender,receiver):
	if request.session.has_key('user'):
		Messages.objects.filter(is_read=False,sender=sender,receiver=receiver).update(is_read=True)
		return JsonResponse({'Result':'Success'})
	else:
		return HttpResponseRedirect("/")


@csrf_exempt
def createAlbumDetails(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			name = request.POST.get('name',"defaultValue")
			
			Updescription=""
			Upaccessibility=""		
			result = createAlbum.objects.filter(Q(userId=request.session['user']) & Q(albumName=name))
			status = ""
			
			# code = str(request.session['user'] + name).encode('utf-8')
			# print(code.hex())
			if result.exists():
				status = "allready"

				album_Id =""
				for i in result:
					album_Id=i.albumId
					Updescription=i.albumDescription
					Upaccessibility=i.albumAccessibility
					break
				imgList = AlbumImageData.objects.filter(albumId=album_Id)
				img = []
				picId = []
				for image in imgList:
					img.append(image.media.url)
					picId.append(image.picAlbumId)
				print(Updescription)
				print(Upaccessibility)
				return JsonResponse({"status":status,"media":img,"picId":picId,"des":Updescription,"access":Upaccessibility})
			else:
				description = request.POST.get('description',"defaultValue")
				accessibility = request.POST.get('accessibility',"defaultValue")
				code = str(request.session['user'] + name).encode('utf-8')
				
				createAlbum(userId=request.session['user'],albumName=name,albumDescription=description,albumAccessibility=accessibility,albumId=code.hex()).save();
				status = "created"
				return JsonResponse({"status":status,"des":Updescription,"access":Upaccessibility})
	else:
		return HttpResponseRedirect("/")

@csrf_exempt
def UploadAlbumImage(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			image = request.FILES.get('theFile')
			Reponame = request.POST.get('repoName',"defaultValue")
			print(Reponame)
			code = str(request.session['user'] + Reponame).encode('utf-8')
			img = []
			picId = []
			t = time.localtime()
			current_time = time.strftime("%H:%M:%S", t)	
			current_time =(str(current_time).encode('utf-8')).hex()+code.hex() 
				
			AlbumImageData(albumId=code.hex(),media=image,picAlbumId=current_time).save()
			return HttpResponseRedirect("/album/")
			# photos = UserPost.objects.filter(userId=request.session['user'])
			# myGallery = createAlbum.objects.filter(userId=request.session['user'])
			# print(myGallery)
			# print("Donnnnnnnnnnnnnne")
			# params = {'photos':photos,'myGallery':myGallery}
			# return render(request,'Album.html',params)
	else:
		return HttpResponseRedirect("/")

@csrf_exempt
def deleteAlbumRepo(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			title = request.POST.get('title',"defaultValue")
			code = str(request.session['user'] + title).encode('utf-8')
			code = code.hex()
			createAlbum.objects.get(albumId = code).delete()
			AlbumImageData.objects.filter(albumId=code).delete()
			return JsonResponse({"Status":"successfully"})
	else:
		return HttpResponseRedirect("/")

@csrf_exempt
def UpdateAlbumRepo(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			name = request.POST.get('name',"defaultValue")
			description = request.POST.get('description',"defaultValue")
			accessibility = request.POST.get('accessibility',"defaultValue")
			code = str(request.session['user'] + name).encode('utf-8')
			query=createAlbum.objects.get(albumId = code.hex())
			query.albumDescription = description
			query.albumAccessibility=accessibility
			query.save()
			return JsonResponse({"Status":"successfully"})
	else:
		return HttpResponseRedirect("/")

@csrf_exempt
def deleteAlbumPicture(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			name = request.POST.get('pic',"defaultValue")
			title = request.POST.get('title',"defaultValue")
			code = str(request.session['user'] + title).encode('utf-8')
			code = code.hex()
			print(name)
			print(title)
			AlbumImageData.objects.filter(picAlbumId=name).delete()
			return JsonResponse({"Status":"successfully"})
	else:
		return HttpResponseRedirect("/")
		

@csrf_exempt
def showProfilePicfun(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			name = request.POST.get("name")
			print(request.session['user'])
			print(name)

			# if name != request.session['user']
			code = str(name + "profile").encode('utf-8')
			code = code.hex()
			profileData = AlbumImageData.objects.filter(albumId = code)
			profilePic = []
			for pic in profileData:
				profilePic.append((pic.media).url)
			# profiledataList = []
			# for item in profileData:
			# 	profiledataList.append(item.media.url)
			# code = str(request.session['user'] + "cover").encode('utf-8')
			# code = code.hex()
			# coverData = AlbumImageData.objects.filter(albumId = code)
			# # coverdataList = []
			# for item in coverData:
			# 	profiledataList.append(item.media.url)
			# print(myGallery)
			# print("photos = ",photos)
			

			params = {'profileData':profilePic,'status':True}
			return JsonResponse(params)
		else:
			return JsonResponse({"status":False})
	else:
		return HttpResponseRedirect("/")

@csrf_exempt
def showCoverPicfun(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			name = request.POST.get("name")
			print(request.session['user'])
			print(name)

			# if name != request.session['user']
			code = str(name + "cover").encode('utf-8')
			code = code.hex()
			coverData = AlbumImageData.objects.filter(albumId = code)
			coverPic = []
			for pic in coverData:
				coverPic.append((pic.media).url)
			# profiledataList = []
			# for item in profileData:
			# 	profiledataList.append(item.media.url)
			# code = str(request.session['user'] + "cover").encode('utf-8')
			# code = code.hex()
			# coverData = AlbumImageData.objects.filter(albumId = code)
			# # coverdataList = []
			# for item in coverData:
			# 	profiledataList.append(item.media.url)
			# print(myGallery)
			# print("photos = ",photos)
			

			params = {'coverData':coverPic,'status':True}
			return JsonResponse(params)
		else:
			return JsonResponse({"status":False})
	else:
		return HttpResponseRedirect("/")


@csrf_exempt
def showPostPicfun(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			name = request.POST.get("name")
			print(request.session['user'])
			print(name)

			# if name != request.session['user']
			
			photos = UserPost.objects.filter(userId=name)
			postPic = []
			postId = []
			for pic in photos:
				if pic.PostType == 'post':
					if pic.post:
						postPic.append((pic.post).url)
						postId.append((pic.postId))
			# profiledataList = []
			# for item in profileData:
			# 	profiledataList.append(item.media.url)
			# code = str(request.session['user'] + "cover").encode('utf-8')
			# code = code.hex()
			# coverData = AlbumImageData.objects.filter(albumId = code)
			# # coverdataList = []
			# for item in coverData:
			# 	profiledataList.append(item.media.url)
			# print(myGallery)
			# print("photos = ",photos)
			

			params = {'postData':postPic,'postId':postId,'status':True}
			return JsonResponse(params)
		else:
			return JsonResponse({"status":False})
	else:
		return HttpResponseRedirect("/")

@csrf_exempt
def showOtherPicfun(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			name = request.POST.get("name")
			qry = createAlbum.objects.filter(userId = name)
			albumName = []
			for item in qry:
				if request.session['user']==name:
					albumName.append(item.albumName)
				elif item.albumAccessibility == "Public":
					albumName.append(item.albumName)
				elif item.albumAccessibility == "My Friends":
					friends = AllFriends.objects.get(userId=request.session['user']).Friends
					if name in friends:
						albumName.append(item.albumName)
			return JsonResponse({"directory":albumName})
	else:
		return HttpResponseRedirect("/")

@csrf_exempt
def showSelectOptionPic(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			name = request.POST.get("name")
			albumName= request.POST.get("username")
			qry = createAlbum.objects.get(Q(albumName=albumName) & Q(userId=name))
			albumPic = []
			if qry:
				if request.session['user']==name:
					qry2 = AlbumImageData.objects.filter(albumId=qry.albumId)
					for item2 in qry2:
						albumPic.append((item2.media).url)
					# albumName.append(item.albumName)
				elif qry.albumAccessibility == "Public":
					qry2 = AlbumImageData.objects.filter(albumId=qry.albumId)
					for item2 in qry2:
						albumPic.append((item2.media).url)
					# albumName.append(item.albumName)
				elif qry.albumAccessibility == "My Friends":
					friends = AllFriends.objects.get(userId=request.session['user']).Friends
					if name in friends:
						qry2 = AlbumImageData.objects.filter(albumId=qry.albumId)
						for item2 in qry2:
							albumPic.append((item2.media).url)
				return JsonResponse({'albumPicUrl':albumPic,'status':True})
		else:
			return JsonResponse({"status":"You are doing something wrong"})
	else:
		return HttpResponseRedirect("/")

def groupCreationForm(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			groupName=request.POST.get("newGroupName")
			groupDescription=request.POST.get("newGroupDescription")
			groupMembers=request.POST.get("newGroupAllFriends")
			groupPic=request.FILES.get('newGroupPic')
			print("groupPic",groupPic)
			print(type(groupPic))
			allFriends = []
			for i in groupMembers.split(","):
				if i!="":
					allFriends.append(i)
			allFriends.append(request.session['user'])
			print(allFriends)
			
			t = time.localtime()
			current_time = time.strftime("%H:%M:%S", t)	
			code = str(request.session['user']+str(current_time)).encode('utf-8')
			code = code.hex()
			
			groupId = code
			for user in allFriends:
				allGroups = userRegistration.objects.get(userId=user).Groups
				allGroups.append(groupId)
				GroupList = allGroups
				print(GroupList,'GroupList')
				userRegistration.objects.filter(userId=user).update(userId=user,Groups=GroupList)
				print("groupPic",groupPic)
			if groupPic:
				Groups(groupId=groupId,groupName=groupName,groupInfo=groupDescription,groupPic=groupPic,
				Members=allFriends).save()
			else:
				Groups(groupId=groupId,groupName=groupName,groupInfo=groupDescription,
				Members=allFriends).save()

			return HttpResponseRedirect("/messages")
	else:
		return HttpResponseRedirect("/")


def groupUpdationForm(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			groupName=request.POST.get("editGroupName")
			groupId=request.POST.get("editFroupgpname")
			groupDescription=request.POST.get("editGroupDescription")
			groupMembers=request.POST.get("editGroupAllFriends")
			groupPic=request.FILES.get('editGroupPic')
			

			allFriends = []
			permission = 0
			for i in groupMembers.split(","):
				if i!="":
					allFriends.append(i)
					print(i)
					if i==request.session['user']:
						permission =1
						print("permission1 = ",i)
			
			print(allFriends)
			
			print("permission2 = ",permission)
			if permission == 1:	
				qry5 = Groups.objects.get(groupId=groupId).Members
				if(qry5[-1] == request.session['user']):
					#Delete Already present Person in Group
					for person in qry5:
						qry6=userRegistration.objects.get(userId=person).Groups
						print("qry6",qry6)
						print("person",person)
						qry6.remove(groupId)
						userRegistration.objects.filter(userId=person).update(Groups=qry6)
					Groups.objects.filter(groupId=groupId).update(Members="")
					#

					for user in allFriends:
						allGroups = userRegistration.objects.get(userId=user).Groups
						allGroups.append(groupId)
						GroupList = allGroups
						print(GroupList,'GroupList')
						userRegistration.objects.filter(userId=user).update(userId=user,Groups=GroupList)
						print("groupPic",groupPic)
					if groupPic:
						Groups.objects.filter(groupId=groupId).update(groupName=groupName,groupInfo=groupDescription,
						Members=allFriends)

						status=Groups.objects.get(groupId=groupId)
						status.groupPic=groupPic
						status.save()
					else:
						Groups.objects.filter(groupId=groupId).update(groupName=groupName,groupInfo=groupDescription,
						Members=allFriends)


			return HttpResponseRedirect("/messages")
	else:
		return HttpResponseRedirect("/")

@csrf_exempt
def leaveGroup(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			gpid=request.POST.get("id")
			qry=Groups.objects.get(groupId=gpid)
			print("qry.Members[-1] = ",qry.Members[-1])
			
			if qry.Members[-1] == request.session['user']:
				for item in qry.Members:
					print("item",item)
					qry1 = userRegistration.objects.get(userId=item).Groups
					print("qry1  = ",qry1)
					qry1.remove(gpid)
					userRegistration.objects.filter(userId=item).update(Groups=qry1)
				Groups.objects.get(groupId=gpid).delete()
			else:
				qry1 = userRegistration.objects.get(userId=request.session['user']).Groups
				qry1.remove(gpid)
				userRegistration.objects.filter(userId=request.session['user']).update(Groups=qry1)
				qry2=Groups.objects.get(groupId=gpid).Members
				qry2.remove(request.session['user'])
				Groups.objects.filter(groupId=gpid).update(Members=qry2)
			
			return JsonResponse({"status":"successfully"})
	else:
		return HttpResponseRedirect("/")


def showPost(request,postid):
	if request.session.has_key('user'):
		postData = UserPost.objects.get(postId=postid)
		allComments = Comments.objects.filter(postId=postid)
		allLikes = Likes.objects.get(postId=postid).postLikedBy
		totalLikes = len(allLikes)
		if request.session['user'] in allLikes:
			colorPost = "rgba(0, 150, 136,1)"
		else:
			colorPost = "grey"
			
		is_authenticated = False
		if str(request.session['user']) == str(postData.userId):
			is_authenticated = True

		print(type(postData.userId))
		print(type(request.session['user']))
		params = {'postData':postData,'allComments':allComments,'is_authenticated':is_authenticated,
		'totalLikes':totalLikes,'colorPost':colorPost,'loggedUser':request.session['user']}
		return render(request,'showPost.html',params)
	else:
		return HttpResponseRedirect('/')

@csrf_exempt
def deshboarDeletePost(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			postId = request.POST.get("postId")
			print(postId)
			UserPost.objects.filter(postId = postId).delete()
			Notifications.objects.filter(postId = postId).delete()
			Likes.objects.filter(postId = postId).delete()
			Comments.objects.filter(postId = postId).delete()
			Replies.objects.filter(postId = postId).delete()
			TaggedPeople.objects.filter(postId = postId).delete()
			return JsonResponse({"status":"success"})		
	else:
		return HttpResponseRedirect("/")

def showPost(request,postid):
	if request.session.has_key('user'):
		postData = UserPost.objects.get(postId=postid)
		allComments = Comments.objects.filter(postId=postid)
		allLikes = Likes.objects.get(postId=postid).postLikedBy
		totalLikes = len(allLikes)
		if request.session['user'] in allLikes:
			colorPost = "rgba(0, 150, 136,1)"
		else:
			colorPost = "grey"
			
		is_authenticated = False
		if str(request.session['user']) == str(postData.userId):
			is_authenticated = True

		print(type(postData.userId))
		print(type(request.session['user']))
		params = {'postData':postData,'allComments':allComments,'is_authenticated':is_authenticated,
		'totalLikes':totalLikes,'colorPost':colorPost,'loggedUser':request.session['user']}
		return render(request,'showPost.html',params)
	else:
		return HttpResponseRedirect('/')

@csrf_exempt
def deshboarDeletePost(request):
	if request.session.has_key('user'):
		if request.method == "POST":
			postId = request.POST.get("postId")
			print(postId)
			UserPost.objects.filter(postId = postId).delete()
			Notifications.objects.filter(postId = postId).delete()
			Likes.objects.filter(postId = postId).delete()
			Comments.objects.filter(postId = postId).delete()
			Replies.objects.filter(postId = postId).delete()
			TaggedPeople.objects.filter(postId = postId).delete()
			return JsonResponse({"status":"success"})		
	else:
		return HttpResponseRedirect("/")


@csrf_exempt
def storyreply(request):
	if request.session.has_key('user'):
		sender = request.session['user']
		receiver = request.POST.get('receiver')
		message = request.POST.get('message')
		messageid = 'privatemessage'+str(uuid.uuid4())
		is_Inbox = Inbox.objects.filter(Users=[sender,receiver]) | Inbox.objects.filter(Users=[receiver,sender])

		if is_Inbox:
			for msg in is_Inbox:
				inboxId = msg.inboxId
		else:
			inboxId = uuid.uuid4().hex
			Inbox(inboxId=inboxId,Users=[myId,friendId]).save()
		Messages(Inbox=Inbox.objects.get(inboxId=inboxId),MessageID=messageid,sender=sender,
		receiver=receiver,is_read=False,Message=message).save()
		return JsonResponse({'Result':'Success'})
	else:
		return HttpResponseRedirect("/")



def aboutUs(request):
	return render(request,'AboutUs.html')


def contactUs(request):
	return render(request,'contactUs.html')


@csrf_exempt
def ContactSubmission(request):
	name=request.POST.get('name')
	email=request.POST.get('email')
	comment=request.POST.get('comment')

	ContactUs(name=name,email=email,comment=comment).save()

	return JsonResponse({"status":"successfully"})

@csrf_exempt
def spamMessageTester(request):
	if request.session.has_key('user'):
		print("Spam")  
		spam=""
		with open('model_pickle','rb') as f:
	         model = pickle.load(f)
	         print(model.predict([request.POST.get('message')]))
	         spam=model.predict([request.POST.get('message')])
	         return JsonResponse({"status":spam.item(0)})#Change numpy ndarray to Single value
	else:
		return HttpResponseRedirect("/")
    
