# coding: utf-8
__author__ = 'Administrator'

from project.models import Project,ProjectItem,Contract,ClaimMaterial,AssignWork,Event


def create_Node(project,date1):
    projectitem=ProjectItem(project_id=project,date=date1)
    projectitem.save()
    return projectitem

def show_Tree(dic,root,height):
    project=Project.objects.get(id=root)
    dic[height]=[]
    dic[height].append([project,0])
    projectitems=ProjectItem.objects.filter(project_id=project.id,parent_id=None,rank__gt=-1,index__gt=-1)
    for item in projectitems:
        dic=traversal_tree(dic,item.id,0)
    return dic

def traversal_tree(dic,root,height):
    try:
        node=ProjectItem.objects.get(id=root)
        node1=node
        temp=0
        index=node.id
        if node.index!=-1:
            node1=ProjectItem.objects.get(id=node.index)
            index=node.index
        if hasattr(node1,'contract'):
            temp=1
        elif hasattr(node1,'claimmaterial'):
            temp=2
        elif hasattr(node1,'assignwork'):
            temp=3
        elif hasattr(node1,'event'):
            temp=4
        if height in dic.keys():
            dic[height].append([node,temp,index])
        else:
            dic[height]=[]
            dic[height].append([node,temp,index])
        childitems=ProjectItem.objects.filter(parent_id=root, rank__gt= -1).order_by('rank')
        for item in childitems:
            traversal_tree(dic,item.id,root)
    except  ProjectItem.DoesNotExist:
        delete_Node(root)
#        pass
    return  dic

def save_Tree(dic):
    for key in dic.keys():
        for v in dic[key]:
            ProjectItem.objects.filter(id=v).update(parent=None,rank=0)
    for key in dic.keys():
        i=0
        while i < len(dic[key]):
            if key==0:
                ProjectItem.objects.filter(id=dic[key][i]).update(rank=i)
            else:
                ProjectItem.objects.filter(id=dic[key][i]).update(parent=ProjectItem.objects.get(id=key),rank=i)
            i=i+1
    return
def add_Node(parent,item_id,parenttype):
    item=ProjectItem.objects.get(id=item_id)
    if int(parenttype)==0:
        ProjectItem(project_id=item.project_id,date=item.date,parent_id=None,rank=len(ProjectItem.objects.filter(parent=None,project_id=parent)),index=item_id).save()
    else:
        ProjectItem(project_id=item.project_id,date=item.date,parent_id=parent,rank=len(ProjectItem.objects.filter(parent_id=parent)),index=item_id).save()
    return

def delete_Node(root):
    node=ProjectItem.objects.get(id=root)
    items=ProjectItem.objects.filter(parent=node.parent)
    for i in items:
        if i.rank>node.rank:
            ProjectItem.objects.filter(id=i.id).update(rank=i.rank-1)
    items=ProjectItem.objects.filter(parent_id=node.id)
    for i in items:
        delete_Node(i.id)
    if node.index==-1:
        ProjectItem.objects.filter(id=node.id).update(parent=None,rank=-1)
    else:
        node.delete()
    return
def traversal_tree_print(root,pro_id):
    array=[]
    try:
        nodes=ProjectItem.objects.filter(project_id=pro_id,parent=root,rank__gt=-1)
        for node in nodes:
            node1=node
            temp=0
            index=node.id
            if node.index!=-1:
                node1=ProjectItem.objects.get(id=node.index)
                index=node.index
            if hasattr(node1,'contract'):
                temp=1
            elif hasattr(node1,'claimmaterial'):
                temp=2
            elif hasattr(node1,'assignwork'):
                temp=3
            elif hasattr(node1,'event'):
                temp=4
            array.append([[node,temp,index],traversal_tree_print(node,pro_id)])
    except ProjectItem.DoesNotExist:
        pass
    return  array