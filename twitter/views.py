from django.shortcuts import render,redirect, get_object_or_404,resolve_url
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import Profile,Tweet,Comment,Followers
from .forms import NewUserForm,ProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

# Create your views here.
site = "http://127.0.0.1:8000/"

def profileRedirect(request):
	if request.user.is_authenticated:
		return redirect(f"{resolve_url('user')}@{request.user.username}")
	else:
		return redirect(resolve_url("login"))


def liketweet(request):
	user = request.user
	tweetid = request.POST.get("ID")
	profile = Profile.objects.get(user=user)
	tweet = Tweet.objects.get(id = tweetid)
	if not profile in tweet.likes.all():
		tweet.likes.add(profile)
	else:
		tweet.likes.remove(profile)
	return redirect(f"{resolve_url('tweet')}{tweetid}")

def follow(request):
	user = request.user
	prof = request.POST.get("ID")
	follower = Profile.objects.get(user=user)
	following = Profile.objects.get(id=prof)
	profilefollower = Followers.objects.get(profileuser=following)
	profilefollowing = Followers.objects.get(profileuser=follower)
	following.user.username
	if not follower in profilefollower.followersprofile.all():
		profilefollower.followersprofile.add(follower)
		profilefollowing.followingprofile.add(following)
	else:
		profilefollower.followersprofile.remove(follower)
		profilefollowing.followingprofile.remove(following)

	return redirect(f"{resolve_url('user')}@{following.user.username}")

def home(request):
    if request.user.is_authenticated:
        return redirect(f"{site}tweets/")
    else:
	    return redirect(f"{site}login/")

def register(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			form = NewUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				login(request, user)
				profile = Profile.objects.create(user = user)
				profile.save()
				followers = Followers.objects.create(profileuser=profile)
				followers.save()
				messages.success(request, "Registration successful." )
				return redirect(f"{site}/profile")
			messages.error(request, "Unsuccessful registration. Invalid information.")
		form = NewUserForm()
		return render (request=request, template_name="twitter/Register.html", context={"register_form":form,"site":site})
	else:
		return redirect(site)

def userLogin(request):
	if not request.user.is_authenticated:
		if request.method == "POST":
			form = AuthenticationForm(request , data =request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				user = authenticate(username = username,password=password)
				if user is not None:
					login(request,user)
					messages.info(request,f"Logged in as {username} ")
					
					return redirect(f"{site}tweets/")
				else:
					messages.error(request,"Invalid username or password")
					form = AuthenticationForm()
					return render(request,"twitter/login.html",{"login_form":form})

			else: 
				messages.error(request,"Invalid username or password")
				form = AuthenticationForm()
				return render(request,"twitter/login.html",{"login_form":form})
		else:		
			form = AuthenticationForm()
			return render(request,"twitter/login.html",{"login_form":form})
	else:
		return redirect(site)


	
def tweets(request):
	if request.user.is_authenticated:
		username = request.user.username
		tweet = Tweet.objects.order_by('-created_time')
		return render(request,"twitter/tweets.html",{"tweets":tweet,"username":username})
	else:
		return redirect(site)

def userLogout(request):
	logout(request)
	messages.info(request,("Logged out successfully"))
	return redirect(site)



def profile(request):
	if request.user.is_authenticated:
		current_profile = Profile.objects.get(user = request.user)
		if request.method == "GET":
			current_profile = Profile.objects.get(user = request.user)
			date = str(current_profile.birth_date)
			fname = current_profile.user.first_name
			lname = current_profile.user.last_name
			followinfo = Followers.objects.get(profileuser = current_profile)
			return render(request,"twitter/profile.html",{"date":date,"bio":current_profile.bio,"f_name":fname,"l_name":lname,"site":site,'image':current_profile.pic.url,'username':request.user.username,"followinfo":followinfo})
		elif request.method == "POST":
			date = request.POST.get("Date_Birth")
			bio = request.POST.get("Bio")
			fname = request.POST.get("fname")
			lname = request.POST.get("lname")
			profilepic = request.FILES.get('profile-pic',False)
			usr = User.objects.get(username = request.user)
			usr.first_name =fname
			usr.last_name = lname
			usr.save()
			pro = Profile.objects.get(user = request.user)
			pro.birth_date = date
			pro.bio = bio
			if profilepic:
				pro.pic = profilepic
			pro.save()
			pro = Profile.objects.get(user = request.user)
			date = str(pro.birth_date)
			bio = pro.bio
			return render(request,"twitter/profile.html",{"date":date,"bio":bio,"f_name":pro.user.first_name,"l_name":pro.user.last_name,"site":site,'image':pro.pic.url,'username':request.user.username})
	else:
		return redirect(f"{site}/login")
		
def createTweet(request):
	if request.user.is_authenticated:
		if request.method == "GET":
			user = request.user.username
			return render(request,"twitter/createtweet.html",{'username':user,'site':site})
		elif request.method == "POST":
			file = request.FILES.get("tweet-pic",False)
			content = request.POST.get("tweet")
			user = Profile.objects.get(user = request.user)
			newtweet = Tweet.objects.create(user=user,content=content)
			if file:
				newtweet.image=file
			else:
				newtweet.image="NULL"
			newtweet.save()
			return redirect(site)
	else:
		return redirect(site)
	
def userpage(request,**kwargs):
	if request.user.is_authenticated:
		requser = kwargs["username"][1:]
		user = get_object_or_404(User,username=requser)
		prof = Profile.objects.get(user=user)
		followinfo = Followers.objects.get(profileuser=prof)
		currprof = Profile.objects.get(user=request.user)
		tweet = Tweet.objects.filter(user=prof)
		return render(request,"twitter/profileview.html",{"username":user.username,"firstname":user.first_name,"lastname":user.last_name,"bio":prof.bio,"dob":prof.birth_date,'image':prof.pic.url,"id":prof.id,"followinfo":followinfo,"tweetinfo":tweet,"currentprofile":currprof,"userprofile":prof})
	else:
		return redirect(resolve_url("Home"))

def tweet(request,**kwargs):
	tweetid = kwargs["tweetid"]
	tweet = get_object_or_404(Tweet,id=tweetid)
	if request.user.is_authenticated:
		if request.method == "GET":
			replies = Comment.objects.filter(tweet = tweet).order_by('-created_time')
			return render(request,"twitter/tweet.html",{'tweet':tweet,'replies':replies,'replycount':len(replies)})
		elif request.method == "POST":
			content = request.POST.get("reply")
			user = Profile.objects.get(user = request.user)
			tweetreply = Comment.objects.create(tweet=tweet,commenter=user,content =content)
			tweetreply.save()
			tweet.replycount = len(Comment.objects.filter(tweet = tweet))
			tweet.save()
			return redirect(f"{site}tweet/{tweetid}")
	else:
		return redirect(site)