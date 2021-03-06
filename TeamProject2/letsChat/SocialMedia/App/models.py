from django.db import models
from datetime import datetime    
from django_mysql.models import ListCharField

GENDERS  = (
            ('M','Male'),
            ('F','Female'),
            ('O','Other'),
            )

class userRegistration(models.Model):
    userId = models.CharField(max_length=50,default='',unique=True,blank=True)
    userName = models.CharField(max_length=50,default='',unique=True,blank=True)
    firstName = models.CharField(max_length=50,default='',blank=True)
    lastName = models.CharField(max_length=50,default='',blank=True)
    mobile = models.CharField(max_length=10,default='',blank=True)
    emailAddress = models.EmailField(max_length=50,default='',blank=True)
    password = models.CharField(max_length=100,default='',blank=True)
    profilePic = models.ImageField(upload_to='media',default='media/profile.jpeg')
    Groups = ListCharField(
        base_field=models.CharField(max_length=50,default='',blank=True),
        max_length=(100 * 100),blank=True
    )
    coverPic = models.ImageField(upload_to='media',default='media/cover.jpg')
    quote = models.CharField(max_length=1000,default='',blank=True)
    dOB = models.CharField(max_length=100,blank=True,default='No birth date to show')
    gender = models.CharField(choices=GENDERS,max_length=1,blank=True)
    countryName = models.CharField(max_length=100,default='',blank=True)
    cityName = models.CharField(max_length=100,default='',blank=True)
    currentEducation = models.CharField(max_length=100,default='',blank=True)
    educationStartYear = models.CharField(max_length=10,default='',blank=True)
    educationEndYear = models.CharField(max_length=10,default='',blank=True)
    companyName = models.CharField(max_length=100,default='',blank=True)
    companyPosition = models.CharField(max_length=100,default='',blank=True)
    companyCity = models.CharField(max_length=50,default='',blank=True)
    companyDescription = models.CharField(max_length=1000,default='',blank=True)
    is_online = models.BooleanField(default=False,blank=True)
    joinedDate = models.DateTimeField(default=datetime.now)
    blueTik=models.BooleanField(default=False,blank=True)

    def __str__(self):
        return self.firstName + ' ' + self.lastName

class Friend_Requests(models.Model):
    sender = models.CharField(max_length=50,default='')
    receiver = models.CharField(max_length=50,default='')
    senderName=models.CharField(max_length=75,default='')
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.senderName

class AllFriends(models.Model):
    userId = models.CharField(max_length=50)
    Friends = ListCharField(
        base_field=models.CharField(max_length=50,blank=True),
        max_length=(100 * 100)
    )

    def __str__(self):
        return self.userId

class Notifications(models.Model):
    postId = models.CharField(max_length=50,blank=True,default='')
    notificationType = models.CharField(max_length=50,default='',blank=True)    # 'friend' for Friend Request 'like' for Like 'comment' for Comment and so on
    fullName = models.CharField(max_length=55, blank=True)
    sender = models.CharField(max_length=55, blank=True)
    receiver = models.CharField(max_length=55, blank=True)
    notification = models.CharField(max_length=100, blank=True)
    viewed = models.BooleanField()
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.fullName    

class UserPost(models.Model):
    PostType = models.CharField(max_length=30,default='',blank=True)
    postId = models.CharField(max_length=100,default='',unique=True) 
    userId = models.CharField(max_length=50,default='')
    userName = models.CharField(max_length=50,default='')
    post = models.FileField(upload_to="profiles",blank=True)
    Message = models.TextField(default="",blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    userPic = models.CharField(max_length=100,default='',blank=True)

class Story(models.Model):
    userId = models.CharField(max_length=50,default='')
    media = models.ImageField(upload_to="profiles",blank=True)
    uploadTime = models.DateTimeField(default=datetime.now, blank=True)
    storyType = models.CharField(max_length=20,default='')
    fontFamily = models.CharField(max_length=75,default='')
    fontSize = models.CharField(max_length=50,default='')
    Caption = models.CharField(max_length=150,default='')
    color = models.CharField(max_length=75,default='')
    
    def __str__(self):
        return self.userId

class Album(models.Model):
    AlbumID = models.CharField(max_length=50,default='',blank=True)
    Name = models.CharField(max_length=50,default='',blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.Name

class Photos(models.Model):
    Album = models.CharField(max_length=50,default='',blank=True)
    PhotoID = models.CharField(max_length=50,default='',blank=True)
    Image = models.ImageField(upload_to='media',blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)


class Likes(models.Model):
    postId = models.CharField(max_length=100,default='',blank=True)
    postLikes = models.IntegerField(default=0,blank=True)
    postLikedBy = ListCharField(
        base_field=models.CharField(max_length=50,default='',blank=True),
        max_length=(100 * 100)
    )
    postLikedOf = models.CharField(max_length=50,default='',blank=True)

    def __str__(self):
        return self.postId

class Inbox(models.Model):
    inboxId = models.CharField(max_length=50,default='',blank=True)
    Users = ListCharField(
        base_field=models.CharField(max_length=50,default='',blank=True),
        max_length=(100 * 100)
    )
    def __int__(self):
        return self.id


class Messages(models.Model):
    Inbox = models.ForeignKey(Inbox,on_delete=models.CASCADE)
    MessageID = models.CharField(max_length=500,default='',blank=True,unique=True)
    sender = models.CharField(max_length=500,default='',blank=True)
    receiver = models.CharField(max_length=500,default='',blank=True)
    is_read = models.BooleanField(default=False,blank=True)
    Message = models.TextField(default='',blank=True)
    date = models.DateTimeField(default=datetime.now,blank=True)
   
class TempRoom(models.Model):
    RoomId = models.CharField(max_length=50,default='',blank=True,unique=True)
    Users = ListCharField(
        base_field=models.CharField(max_length=50,default='',blank=True),
        max_length=(100 * 100)
    )

    def __str__(self):
        return self.RoomId

class Groups(models.Model):
    groupId = models.CharField(max_length=50,default='',blank=True)
    groupName = models.CharField(max_length=50,default='',blank=True)
    Members = ListCharField(
        base_field=models.CharField(max_length=50,default='',blank=True),
        max_length=(100 * 100)
    )
    groupInfo = models.CharField(max_length=50,default='',blank=True)
    groupPic = models.ImageField(upload_to='media',default='media/group.png',blank=True)
    def __str__(self):
        return self.groupName

class GroupChat(models.Model):
    groupId = models.CharField(max_length=50,default='',blank=True)
    Group = models.ForeignKey(Groups,on_delete=models.CASCADE,default=1)
    messageID = models.CharField(max_length=50,default='',blank=True,unique=True)
    Message = models.TextField(default='',blank=True)
    sender = models.CharField(max_length=500,default='',blank=True)
    senderName = models.CharField(max_length=50,default='',blank=True)
    senderPic = models.CharField(max_length=50,default='',blank=True)
    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now,blank=True)

    def __list__(self):
        return self.Members

class Comments(models.Model):
    postId = models.CharField(max_length=100,default='',blank=True)
    commentId = models.CharField(max_length=100,default='',blank=True,unique=True)
    comment = models.TextField(default='',blank=True)
    commentedBy = models.CharField(max_length=500,default='',blank=True)
    commentedOf = models.CharField(max_length=50,default='',blank=True)
    date = models.DateTimeField(default=datetime.now,blank=True)
    userInfo = models.ForeignKey(userRegistration,on_delete=models.CASCADE)

    def __str__(self):
        return self.postId

class Replies(models.Model):
    postId = models.CharField(max_length=50,default='',blank=True)
    commentId = models.CharField(max_length=50,default='',blank=True)
    replyId = models.CharField(max_length=50,default='',blank=True)
    repliedBy = models.CharField(max_length=50,default='',blank=True)
    repliedOn = models.CharField(max_length=50,default='',blank=True)
    reply = models.CharField(max_length=50,default='',blank=True)
    date = models.DateTimeField(default=datetime.now,blank=True)
    userInfo = models.ForeignKey(userRegistration,on_delete=models.CASCADE)

    def __str__(self):
        return self.postId

#For Report
class Report(models.Model):
    postId = models.CharField(max_length=100,default='')
    reportTitle= models.CharField(max_length=100,default='')
    status = models.BooleanField(default=False)

class TaggedPeople(models.Model):
    taggedId = models.CharField(max_length=50,default='',blank=True)
    taggedPersons = ListCharField(
        base_field=models.CharField(max_length=50,default='',blank=True),
        max_length=(100 * 100)
    )
    postId = models.CharField(max_length=50,default='',blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.taggedId

class createAlbum(models.Model):
    userId = models.CharField(max_length=75,default='')
    albumName = models.CharField(max_length=75,default='')
    albumDescription = models.CharField(max_length=250,default='')
    albumAccessibility = models.CharField(max_length=75,default='')
    albumId = models.CharField(max_length=200,default='')


class AlbumImageData(models.Model):
    media = models.ImageField(upload_to="profiles",blank=True)
    albumId = models.CharField(max_length=200,default='')
    picAlbumId = models.CharField(max_length=200,default='')


class ContactUs(models.Model):
    ContactId = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default='')
    email=models.EmailField(max_length=50,default='',blank=True)
    comment=models.CharField(max_length=1000,default='')
    date = models.DateTimeField(default=datetime.now, blank=True)