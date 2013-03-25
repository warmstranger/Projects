#coding= utf-8

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from api import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.conf import settings

def home(request):
    return redirect('/tree/show_tree')

def create_node_type(request,parenttype,root):
    EVENTS = {
        1: '合同',
        2: '领料',
        3: '派工',
        4: '事件',
        }
    context = {'event': EVENTS,'parenttype':parenttype,'root':root}
    return render_to_response('add_node.html', RequestContext(request, context))

@csrf_protect
def create_node(request):
    event_type = request.POST['event_type']
    root = request.POST['root']
    parenttype=request.POST['parenttype']
    context={'parent':root,'parenttype':parenttype}
    if int(parenttype)==0:
        pro_id=Project.objects.get(id=root)
    else:
        pro_id=ProjectItem.objects.get(id=root).project_id
    if int(event_type) == 1:
        context['projectitem']=Contract.objects.filter(project_id=pro_id)
        context['type']=1
    elif int(event_type) == 2:
        context['projectitem']=ClaimMaterial.objects.filter(project_id=pro_id)
        context['type']=2
    elif int(event_type) == 3:
        context['projectitem']=AssignWork.objects.filter(project_id=pro_id)
        context['type']=3
    elif int(event_type) == 4:
        context['projectitem']=Event.objects.filter(project_id=pro_id)
        context['type']=4
    return render_to_response('event_choice.html', RequestContext(request, context))

def add_node(request):
    parent=request.POST['parent']
    item=request.POST['item']
    parenttype=request.POST['parenttype']
    add_Node(parent,item,parenttype)
    return redirect('/tree/show_tree')

def show_tree(request):
    projects=Project.objects.all()
    #    projecttree=ProjectTree.objects.all()
    context={'projects':projects}
    return render_to_response('show_tree.html', RequestContext(request, context))

def show_projecttree(request,root):
    dic={}
    dic=show_Tree(dic,root,-1)
    return render_to_response('show_projecttree.html',RequestContext(request,{'dic':dic,'root':root}))

def delete_node(request,root):
    pro_id=ProjectItem.objects.get(id=root).project_id
    delete_Node(root)
    s='/tree/show_tree/'+str(pro_id)+'/'
    return redirect(s)

def save_tree(request):
    tree=request.POST['tree']
    root=request.POST['root']
    tree1=tree.split(';')
    dic = {}
    for t in tree1:
        if t!='':
            temp = t.split(':')
            temp1 =temp[1].split(',')
            if '_' in temp[0]:
                temp[0]=0
            array=[]
            for i in temp1:
                if i!='':
                    array.append(int(i))
            dic[temp[0]]=array
    save_Tree(dic)
    str='/tree/show_tree/'+root+'/'
    return redirect(str)

def download_file(request,root):
    font_dir = settings.TTC_PATH
    ParagraphStyle.defaults['wordWrap']="CJK"
    pdfmetrics.registerFont(TTFont('song', font_dir))
    response = HttpResponse(mimetype='application/pdf')
    pro_name=Project.objects.get(id=root).name
    response['Content-Disposition'] = 'attachment; filename=project.pdf'
    p = canvas.Canvas(response)
    p.setFont('song',30)
    p.drawString(150,750,pro_name)
    p.setFont('song',20)
    array=traversal_tree_print(None,root)
    outline_tree(array,0,p,30,600)
    p.showPage()
    p = traversal_print_tree(root,0,p,0);
    p.showOutline()
    p.save()
    return response

def traversal_print_tree(root,flag,p,height):
    project_dir = settings.MEDIA_ROOT
    scan_document_width = 600
    scan_document_height = 750
    font_name = 'song'
    title_font_size = 16
    content_font_size = 12
    if flag:
        node=ProjectItem.objects.get(id=root)
        if node.index!=-1:
            index_node = ProjectItem.objects.get(id=node.index)
        else:
            index_node = node
        if hasattr(index_node,'contract'):
            contract = Contract.objects.get(id=node.index)
            p.setFont(font_name, content_font_size)
            p.drawString(30,800,"合同扫描件:")
            p.drawImage(project_dir+str(contract.scan_document),0,0,scan_document_width,scan_document_height)
            key = '%s' % str(node.id)
            p.bookmarkPage(key)
            p.addOutlineEntry('合同扫描件',key, height, 0)
            p.addPageLabel(p.getPageNumber())
            p.showPage()
        elif hasattr(index_node,'claimmaterial'):
            claimMaterial = ClaimMaterial.objects.get(id=node.index)
            claimMaterial.description
            p.setFont(font_name, title_font_size)
            p.drawString(260,775,"领料")
            p.setFont(font_name, content_font_size)
            p.drawString(30,750,"日期:")
            p.drawString(100,750,str(claimMaterial.date))
            p.drawString(30,725,"领料人:")
            p.drawString(100,725,str(claimMaterial.claimer))
            p.drawString(30,700,"费用:")
            p.drawString(100,700,str(claimMaterial.price))
            p.drawString(30,675,"描述:")
            p.drawString(100,675,claimMaterial.description)
            key = '%s' % str(node.id)
            p.bookmarkPage(key)
            p.addOutlineEntry('领料',key, height, 0)
            p.addPageLabel(p.getPageNumber())
            p.showPage()
        elif hasattr(index_node,'assignwork'):
            assignWork = AssignWork.objects.get(id=node.index)
            p.setFont(font_name, title_font_size)
            p.drawString(260,775,"派工")
            p.setFont(font_name, content_font_size)
            p.drawString(30,750,"日期:")
            p.drawString(100,750,str(assignWork.date))
            key = '%s' % str(node.id)
            p.bookmarkPage(key)
            p.addOutlineEntry('派工',key, height, 0)
            p.addPageLabel(p.getPageNumber())
            p.showPage()
            #派工单扫描
            if assignWork.assign_work_sheet:
                p.setFont(font_name, 12)
                p.drawString(30,800,"派工单扫描件:")
                p.drawImage(project_dir+str(assignWork.assign_work_sheet.scan_document),0,0,scan_document_width,scan_document_height)
                key =  'assign%s' % str(assignWork.assign_work_sheet_id)
                p.bookmarkPage(key)
                p.addOutlineEntry('派工单扫描件',key, height+1, 0)
                p.addPageLabel(p.getPageNumber())
                p.showPage()
            if assignWork.acceptance_sheet:
                p.setFont(font_name, title_font_size)
                p.drawString(260,775,"验收单")
                p.setFont(font_name, content_font_size)
                p.drawString(30,750,"验收要求:")
                p.drawString(100,750,assignWork.acceptance_sheet.requirement)
                p.drawString(30,725,"其他要求:")
                p.drawString(100,725,assignWork.acceptance_sheet.other_requirement)
                p.drawString(30,700,"验收情况:")
                p.drawString(100,700,assignWork.acceptance_sheet.status)
                p.drawString(30,675,"验收日期:")
                p.drawString(100,675,str(assignWork.acceptance_sheet.check_date))
                p.drawString(30,650,"完工日期:")
                p.drawString(100,650,str(assignWork.acceptance_sheet.finish_date))
                key =  'accept%s' % str(assignWork.acceptance_sheet_id)
                p.bookmarkPage(key)
                p.addOutlineEntry('验收单',key, height+1, 0)
                p.showPage()
            if assignWork.bidding_sheet:
                p.setFont(font_name, title_font_size)
                p.drawString(260,775,"报价单")
                p.setFont(font_name, content_font_size)
                p.drawString(30,750,"日期:")
                p.drawString(100,750,str(assignWork.bidding_sheet.date))
                p.drawString(30,725,"工作内容:")
                p.drawString(100,725,assignWork.bidding_sheet.description)
                key =  'bidding%s' % str(assignWork.bidding_sheet_id)
                p.bookmarkPage(key)
                p.addOutlineEntry('报价单',key, height+1, 0)
                p.addPageLabel(p.getPageNumber())
                p.showPage()
            if assignWork.estimate_sheet:
                p.setFont(font_name, content_font_size)
                p.drawString(30,800,"估价单扫描件:")
                p.drawImage(project_dir+str(assignWork.estimate_sheet.scan_document),0,0,scan_document_width,scan_document_height)
                key = 'estimate%s' % str(assignWork.estimate_sheet_id)
                p.bookmarkPage(key)
                p.addOutlineEntry('估价单扫描件',key, height+1, 0)
                p.addPageLabel(p.getPageNumber())
                p.showPage()
            if assignWork.payment:
                payment = assignWork.payment
                p.setFont(font_name, title_font_size)
                p.drawString(260,775,"支付单")
                p.setFont(font_name, content_font_size)
                p.drawString(30,750,"申请日期:")
                p.drawString(100,750,str(payment.date))
                p.drawString(30,725,"申请部门:")
                p.drawString(100,725,str(payment.department))
                p.drawString(30,700,"经办人:")
                p.drawString(100,700,str(payment.operator))
                p.drawString(30,675,"账号:")
                p.drawString(100,675,payment.account)
                p.drawString(30,650,"支付对象:")
                p.drawString(100,650,str(payment.provider))
                p.drawString(30,625,"支付金额:")
                p.drawString(100,625,payment.amount)
                p.drawString(30,600,"费用编号:")
                p.drawString(100,600,str(payment.number))
                p.drawString(30,575,"类别:")
                p.drawString(100,575,str(payment.category))
                p.drawString(30,550,"支付内容:")
                p.drawString(100,550,payment.description)
                key = '%s' % str(payment.id)
                p.bookmarkPage(key)
                p.addOutlineEntry('支付单',key, height+1, 0)
                p.addPageLabel(p.getPageNumber())
                p.showPage()
        elif hasattr(index_node,'event'):
            event = Event.objects.get(id=node.index)
            p.setFont(font_name, title_font_size)
            p.drawString(260,775,"事件")
            p.setFont(font_name, content_font_size)
            p.drawString(30,750,"日期:")
            p.drawString(100,750,str(event.date))
            p.drawString(30,725,"描述:")
            p.drawString(100,725,event.description)
            key =  '%s' % str(node.id)
            p.bookmarkPage(key)
            p.addOutlineEntry('事件',key, height, 0)
            p.addPageLabel(p.getPageNumber())
            p.showPage()
        childitems=ProjectItem.objects.filter(parent_id=root).order_by('rank')
    else:
        node=Project.objects.get(id=root)
        childitems=ProjectItem.objects.filter(project_id=node.id,parent_id=None,rank__gt=-1,index__gt=-1).order_by('rank')
        p.setFont(font_name, title_font_size)
        p.drawString(260,775,"项目")
        p.setFont(font_name, content_font_size)
        p.drawString(30,750,"项目类型:")
        if node.type:
            p.drawString(100,750,"技改")
        else:
            p.drawString(100,750,"基建")
        p.drawString(30,725,"项目名称:")
        p.drawString(100,725,node.name)
        p.drawString(30,700,"项目主管:")
        p.drawString(100,700,str(node.manager))
        p.drawString(30,675,"项目投资:")
        p.drawString(100,675,str(node.investment))
        p.drawString(30,650,"日期:")
        p.drawString(100,650,str(node.date))
        p.drawString(30,625,"项目批复:")
        p.drawString(100,625,node.reply)
        p.drawString(30,600,"项目简介:")
        p.drawString(100,600,node.description)
        key = '%s' % str(node.id)
        p.bookmarkPage(key)
        p.addOutlineEntry('项目',key, height, 0)
        p.addPageLabel(p.getPageNumber())
        p.showPage()
    for item in childitems:
        p = traversal_print_tree(item.id,1,p,height+1)
    return p

def outline_tree(array,space,p,x,y):
    i=0
    if y<=20:
        p.showPage()
        y=700
    while i<len(array):
        if(int(array[i][0][1])==1):
            p.linkAbsolute(str(array[i][0][0].id),str(array[i][0][0].id),(x,y+20,x+1000,y))
            p.drawString(x,y,str(array[i][0][0].date)+str(',合同'))
        elif(int(array[i][0][1])==2):
            p.linkAbsolute(str(array[i][0][0].id),str(array[i][0][0].id),(x,y+20,x+1000,y))
            p.drawString(x,y,str(array[i][0][0].date)+str(',领料'))
        elif(int(array[i][0][1])==3):
            p.linkAbsolute(str(array[i][0][0].id),str(array[i][0][0].id),(x,y+20,x+1000,y))
            p.drawString(x,y,str(array[i][0][0].date)+str(',派工'))
        elif(int(array[i][0][1])==4):
            p.linkAbsolute(str(array[i][0][0].id),str(array[i][0][0].id),(x,y+20,x+1000,y))
            p.drawString(x,y,str(array[i][0][0].date)+str(',事件'))
        y=outline_tree(array[i][1],space+10,p,x+20,y-25)
        i=i+1
    return y
