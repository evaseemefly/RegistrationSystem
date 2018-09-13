from rest_framework.views import APIView

from .models import R_Author_Department

class AuthDepartmentBaseView(APIView):
    def getDeparmetnlistbyAuth(self,userid):
        '''
        根据用户id，获取该用户所属的department
        :param userid:
        :return:
        '''
        if userid > -1:
            department_list=[r.did for r in R_Author_Department.objects.filter(aid=userid)]
        return department_list