from django.shortcuts import redirect

class CustomizedRquirementLogin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
<<<<<<< HEAD
<<<<<<< HEAD
            return redirect("account:login")
=======
            return redirect("user:login")
>>>>>>> 15a2cd7 (update Attendance logic and fix some bugs)
=======
            return redirect("account:login")
>>>>>>> origin/main
        return super(CustomizedRquirementLogin, self, ).dispatch(request, *args, **kwargs)