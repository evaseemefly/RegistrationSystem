/**
 * Created by evase on 2017/9/29.
 */

    //要素
var Element = function(id, name) {
        this.Id = id;
        this.Name = name
    }

//层级
var Level = function(id, name, eid) {
    this.Id = id;
    this.Name = name;
    this.Eid = eid;
}
//时效（此处起名为间隔）
var Interval = function(id, name, lid) {
    this.Id = id;
    this.Name = name;
    this.Lid = lid;
}

function ElementViewModel(elements,levels,intervals) {
    //根据传入的数组生成级联对象
    self = this;
    self.Element = ko.observable();
    self.Level = ko.observable();
    self.Interval = ko.observable();

    // self.Element_test = ko.observable();
    // self.Level_test = ko.observable();
    // self.Interval_test = ko.observable();
//				{"id":1,"name":"风暴潮"}
    //通过读取数据库实现级联菜单，以下部分以后不用

    self.ElementList = ko.observableArray([
        new Element(1, "海浪"),
        new Element(2, "风"),
        new Element(3, "海流"),
        new Element(4, "气压"),
    ]);
    self.LevelList = ko.observableArray([
        new Level(1, "地面", 2),
        new Level(2, "250", 2),
        new Level(3, "500", 2),
        new Level(4, "700", 2),
        new Level(5, "850", 2)
    ]);
    self.IntervalList = ko.observableArray([
        new Interval(1, "0", 2),
        new Interval(6, "6", 2),
    ]);

    self.ElementList = ko.observableArray(elements);
	self.LevelList = ko.observableArray(levels);
	self.IntervalList = ko.observableArray(intervals);

    self.CurrentLevelList = ko.computed(function() {
        return ko.utils.arrayFilter(self.LevelList(), function(level) {
            return level.Eid == self.Element();
        });
    }, self);

    self.CurrentIntervalList = ko.computed(function() {
        return ko.utils.arrayFilter(self.IntervalList(), function(interval) {
            return interval.Lid == self.Level();
        });
    }, self);


    self.getData=function () {
        var data={
            element: self.Element(),
            level:self.Level(),
            interval: self.Interval()
        }
        return data;
    }
}