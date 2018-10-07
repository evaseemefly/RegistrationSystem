/**
 * Created by evase on 2017/10/10.
 */

function BaseInfoViewModel(){
    var self=this;
    self.targetdate=ko.observable(2013040100);

    self.getData=function () {
        var data={
            targetdate: self.targetdate()
        }
        return data;
    }
}