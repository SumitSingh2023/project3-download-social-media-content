import instaloader
ig=instaloader.Instaloader()
req_user=input("req user name: ")
ig.download_profile(req_user,profile_pic=True)