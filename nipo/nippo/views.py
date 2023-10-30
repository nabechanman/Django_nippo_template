from django.shortcuts import render


def nippoListView(request):
    template_name = "nippo/nippo-list.html"
    ctx = {}

    if request.POST:
        text = request.POST.get("text", "")
        name = request.POST.get("name", "")
        content = request.POST.get("content", "")
        input1_date = request.POST.get("input1_date", "")
        input1_time1 = request.POST.get("input1_time1", "")
        input1_time2 = request.POST.get("input1_time2", "")

        input2_date = request.POST.get("input2_date", "")
        input2_time1 = request.POST.get("input2_time1", "")
        input2_time2 = request.POST.get("input2_time2", "")

        input3_date = request.POST.get("input3_date", "")
        input3_time1 = request.POST.get("input3_time1", "")
        input3_time2 = request.POST.get("input3_time2", "")

        ctx["text"] = text
        ctx["nn"] = name
        ctx["content"] = content


    if input1_date:
        s = str(input1_date).split("-")
        p1 = s[1] + "月" + s[2] + "日"
    else:
        p1 = ""

    ctx["input1_date"] = p1
    ctx["input1_time1"] = input1_time1
    ctx["input1_time2"] = input1_time2

   
    if input2_date:
        s = str(input2_date).split("-")
        p2 = s[1] + "月" + s[2] + "日"
    else:
        p2 = ""

    ctx["input2_date"] = p2
    ctx["input2_time1"] = input2_time1
    ctx["input2_time2"] = input2_time2

    if input3_date:
        s = str(input3_date).split("-")
        p3 = s[1] + "月" + s[2] + "日"
    else:
        p3 = ""

    ctx["input3_date"] = p3
    ctx["input3_time1"] = input3_time1
    ctx["input3_time2"] = input3_time2

    return render(request, template_name, ctx)
