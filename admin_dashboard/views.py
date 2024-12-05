from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from admin_dashboard.models import tbl_user,Role,Permission1


# Create your views here.
def user_management_view(request):
    return render(request,'dashboard.html')
def users(request):
    us1 = tbl_user.objects.all()
    roles = Role.objects.values('id','Role_name').distinct()
    return render(request,'user_management.html',{'users':us1,'roles': roles})
def add_user(request):
    if request.method == 'POST':
        us = tbl_user()
        us.Username = request.POST.get('username')
        us.Email = request.POST.get('email')
        role_id = request.POST.get('role')
        us.Roles = Role.objects.get(id=role_id) if role_id else None
        us.Status = request.POST.get('status')
        us.save()
        messages.success(request,'Successfully Saved') 
        return redirect('/user1')
    roles = Role.objects.all()
    return render(request, 'user_management.html', {'roles': roles})
def edit_user(request,id):
    edt = tbl_user.objects.get(id=id)
    roles = Role.objects.all() 
    return render(request,'edit_user.html',{'edt_user':edt, 'roles': roles})
def edit_user2(request,id):
    ed = tbl_user.objects.get(id = id)
    role = Role.objects.get(id = request.POST.get('role'))
    ed.Username = request.POST.get('username')
    ed.Email = request.POST.get('email')
    # ed.Roles = request.POST.get('role')
    ed.Status = request.POST.get('status')
    ed.save()
    messages.success(request,'Successfully Updated')
    return redirect('/user1')
def delete_user(request,id):
    lg = tbl_user.objects.get(id=id)
    lg.delete()
    return redirect('/user1')
def role_manager(request):
    rl = Role.objects.prefetch_related('Assigned_permission').all()
    unique_permission = Permission1.objects.filter(Status="active").distinct()

    return render(request,'role_management.html',{'rle':rl,'permissions': unique_permission})
def add_role(request):
    unique_permission = Permission1.objects.filter(Status="active").distinct()
    if request.method == 'POST':
        Role_name = request.POST.get('role_name')
        Description = request.POST.get('Description')
        Status = request.POST.get('status')
        selected_permissions = request.POST.getlist('permissions')
        role = Role(Role_name=Role_name,Description=Description,Status=Status)
        role.save()
        permissions = Permission1.objects.filter(id__in=selected_permissions)
        role.Assigned_permission.set(permissions)
        return redirect('/rolemanage')
    return render(request,'role_management.html', {'permissions': unique_permission})
def delete_role(request,id):
    dl = Role.objects.get(id=id)
    dl.delete()
    return redirect('/rolemanage')
def edit_role(request,id):
    edtrle = Role.objects.get(id=id)
    permissions = Permission1.objects.all()
    return render(request,'edit_role.html',{'rleedit':edtrle, 'permissions': permissions})
def edit_role2(request,id):
    if request.method == 'POST':
        role = Role.objects.get(id=id)
        role.Description = request.POST.get('Description')
        role.Status = request.POST.get('status')
        role.save()
        permissions = request.POST.getlist('permissions')
        role.Assigned_permission.set(permissions)
        role.save()
        return redirect('/rolemanage')
def permission_manager(request):
    ps1 = Permission1.objects.all()
    return render(request,'permission_management.html',{'ps':ps1})
def add_permission(request):
    if request.method == 'POST':
        pr = Permission1()
        pr.Name = request.POST.get('Permission')
        pr.description = request.POST.get('description')
        pr.Status = "Active"
        pr.save()
        return redirect('/permissionmanage')
    else:
        return HttpResponse('occured error')
def edit_permission(request,id):
    predt = Permission1.objects.get(id=id)
    return render(request,'edit_permission.html',{'pedit':predt})
def edit_permission2(request,id):
    pd = Permission1.objects.get(id = id)
    # pd.Name = request.POST.get('Permission')
    pd.description = request.POST.get('description')
    pd.save()
    return redirect('/permissionmanage')
def delete_permission(request,id):
    pd1 = Permission1.objects.get(id=id)
    pd1.delete()
    return redirect('/permissionmanage')



