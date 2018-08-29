/**
 *
 *
 * @export
 * @class Department
 */
export class Department {
  constructor(pid, did, name) {
    this.pid = pid;
    this.did = did;
    this.name = name;
  }
}

/**
 *  提交给后台查询指定部门、指定日期的值班信息
 *
 * @export
 * @class DepartmentMid
 */
export class DepartmentMid {
  constructor(did, date) {
    this.did = did;
    this.selectedDate = date;
  }
}

/**
 * 在main-content中显示的值班人员相关信息
 *
 * @export
 * @class User
 */
export class User {
  constructor(name, level, desc, group, duty, img_url) {
    this.name = name;
    this.level = level;
    this.desc = desc;
    this.group = group;
    this.duty = duty;
    this.img_url = img_url;
  }
}