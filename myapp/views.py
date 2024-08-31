from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from .models import APTEST
from .models import project
from .models import etat_project
from .models import operation
from django.core.paginator import Paginator
# Create your views here.
def app_view(request,id_projet):
    url =id_projet
    if request.method == 'GET':

        
        proj=project.objects.get(id_project=url)
        
        operations = operation.objects.filter(id_project_id=proj.id_project)
        pag=Paginator(operations,"3")
        pag_nbr=request.GET.get('page')
        pag_obj=pag.get_page(pag_nbr)
        print('t(this)',operations)
        return render(request,'myapp/insertion_op_table.html',{'id_projet': url,'opr_list':operations,'opr_pg':pag_obj})
def add_op(request,id_projet):
    url =id_projet
    if request.method == 'POST':
      libelle=request.POST.get('libelle')
      obj_vise=request.POST.get('Obj_vise')
      anne_MF=request.POST.get('yearpicker_MF')
      anne_indiv=request.POST.get('yearpicker_indiv')
      ap_init=request.POST.get('ap')
      ap_act=request.POST.get('ap_act')
      cml_eng=request.POST.get('Cml_eng')
      cml_pai=request.POST.get('Cml_pai')
      Cntr=request.POST.get('Contraintes')
      if not libelle or not obj_vise or not anne_MF or not anne_indiv or not ap_init or not ap_act or not cml_eng or not cml_pai:
        print('error fo request ',libelle)
        return render(request,'myapp/insertion_op_table.html',{'error':'required field'})
      print('accepted in ',libelle)
      num=libelle+"1"
      taux=float(cml_pai)/float(cml_eng)
      proj=project.objects.get(id_project=url)
      operation.objects.create(id_libelle_op=libelle,
      num_op=num,
      object_vise_po=obj_vise,
      notifcation_an_MF_op=anne_MF,
      indiv_an_op=anne_indiv,
      AP_init_op=ap_init,
      AP_real_op=ap_act,
      cum_AP_eng_an_op=cml_eng,
      cum_AP_pai_an_op=cml_pai,
      taux_real_ph_an_op=taux,
      date_cre_op=date.today(),
      id_project=proj,
      )
      proj=project.objects.get(id_project=url)
      operations = operation.objects.filter(id_project_id=proj.id_project)
      return redirect('app_view',id_projet= url)
    return render(request,'myapp/insertion_op_table.html',{'id_projet': url})
def proj_add(request):
    proj=project.objects.all()
    if request.method == 'GET':
        exist=request.GET.get('exist')
        nv=request.GET.get('nouvel')
        if exist:
            print('show me drop down')
            lis_proj = project.objects.values_list('id_project', flat=True)
#            lis_proj=[
#    {"name": "Project A", "type": "type1", "description": "Description for Project A"},
#    {"name": "Project B", "type": "type1", "description": "Description for Project B"},
#    {"name": "Project C", "type": "type2", "description": "Description for Project C"},
#    {"name": "Project D", "type": "type2", "description": "Description for Project D"},
#    {"name": "Project E", "type": "type3", "description": "Description for Project E"},
#]
            
            print(lis_proj)
            pgs=Paginator(lis_proj,"3")
            pgs_nbr=request.GET.get('page')
            pgs_lst=pgs.get_page(pgs_nbr)
            return render(request,'myapp/insertion_pr_table.html',{'exist':exist,'project':lis_proj,'list_projet':proj,'list_prpg':pgs_lst})
        if nv:
            print('new project show forms')
            return render(request,'myapp/insertion_pr_table.html',{'nouvel':nv,'list_projet':proj})
        if not exist and not nv:
            
            return render(request,'myapp/insertion_pr_table.html',{'list_projet':proj})
    if request.method == 'POST':
        libl=request.POST.get('libelle_pr')
        numindv=request.POST.get('Num-indv')
        ap_act=request.POST.get('ap')
        dp_cml=request.POST.get('dp_cm')
        pec=request.POST.get('PEC')
        dp_prev=request.POST.get('dp_prev')
        current_date = date.today()
        etat=etat_project.objects.get(id_etat=0)
        if not libl or not numindv or not ap_act or not dp_cml or not pec or not dp_prev:
            print('errore request POST',libl)
        print('success',etat.id_etat)
        project.objects.create(Libelle=libl,num_indiv=numindv,AP_Act=ap_act,dp_cum=dp_cml,PEC=pec,dp_prev=dp_prev,date_chng=current_date,etat_project=etat)
        return render(request,'myapp/insertion_pr_table.html',{'successs':'ajouter Projet','list_projet':proj})
@csrf_exempt
def proj_update(request):
    if request.method == 'POST':
        libl=request.POST.get('Libelle')
        numindv=request.POST.get('num_indiv')
        ap_act=request.POST.get('AP_Act')
        dp_cml=request.POST.get('dp_cum')
        pec=request.POST.get('PEC')
        dp_prev=request.POST.get('dp_prev')
        current_date = date.today()
        etat=etat_project.objects.get(id_etat=0)
        return JsonResponse({'status': 'success', 'message': 'Data received!'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
@csrf_exempt
def opr_update(request):
    if request.method == 'POST':
        id_libelle_op=request.POST.get('id_libelle_op')
        num_op=request.POST.get('num_op')
        object_vise_po=request.POST.get('object_vise_po')
        notifcation_an_MF_op=request.POST.get('notifcation_an_MF_op')
        indiv_an_op=request.POST.get('indiv_an_op')
        AP_init_op=request.POST.get('AP_init_op')
        AP_real_op=request.POST.get('AP_real_op')
        cum_AP_eng_an_op=request.POST.get('cum_AP_eng_an_op')
        cum_AP_pai_an_op=request.POST.get('cum_AP_pai_an_op')
        taux_real_ph_an_op=request.POST.get('taux_real_ph_an_op')
        date_cre_op=request.POST.get('date_cre_op')
        current_date = date.today()
        etat=etat_project.objects.get(id_etat=0)
        return JsonResponse({'status': 'success', 'message': 'Data received!'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
        

        
        
