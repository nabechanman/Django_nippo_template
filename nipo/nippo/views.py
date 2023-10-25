from django.shortcuts import render

def nippoListView(request):
	template_name="nippo/nippo-list.html"

	if request.POST:
		text = request.POST.get("text","")
		name = request.POST.get("name","")
		date = request.POST.get("date","")

		input1_date = request.POST.get("input1_date","")
		input1_time1 = request.POST.get("input1_time1","")
		input1_time2 = request.POST.get("input1_time2","")


	else :
		text = ""
		name = ""
	ctx={}	
	ctx["text"] = text
	ctx["nn"] = name
	ctx["date"]= date

	ctx["input1_date"]  = input1_date
	ctx["input1_time1"] = input1_time1
	ctx["input1_time2"] = input1_time2

	return render(request,template_name,ctx )

