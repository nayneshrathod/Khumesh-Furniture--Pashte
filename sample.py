from django.contrib.auth.models import User
from blogs.models import post
from extapp.models import extenduser

s = User.objects.get(username='Nano')
d = post.objects.create(post_writer=s, post_title='This is a Post Title', post_description='this is a post Discription',
                        post_publish_status=True)
d.save

d1 = post.objects.create(post_writer=s, post_title='This is a Post Title',
                         post_description='this is a post Discription by Naynesh', post_publish_status=True)
d1.save

s1 = User.objects.get(username='Koli')
b = post.objects.create(post_writer=s1, post_title='This is a Post Title by Koli',
                        post_description='this is a post Discription by Koli', post_publish_status=True)
b.save

b1 = post.objects.create(post_writer=s1, post_title='This is a Post Title by Koli',
                         post_description='this is a post Discription by Koli', post_publish_status=False)
b1.save

data = extenduser.objects.all()
dataa = data[0:3]

data1 = extenduser.objects.get(user=2)
print(data1.profile_pic)

# dataa = User.objects.filter(id=request.user.id)
# data = extenduser.objects.all()
# dataa = data[0:3]

# print(dataa)
# print(dataa.get(id=request.user.id))
#
# datac = extenduser.objects.get(user__username=dataa.get(id=request.user.id))
# print(str(datac))
