-- drop database if exists Edith;

create database if not exists Edith;

use Edith;

drop table if exists user;

CREATE TABLE user_user (
    id INT unsigned auto_increment primary key comment '用户编号',
    username varchar(20) not null unique comment '用户名',
    phone char(11) not null unique comment '电话',
    password char(32) not null comment '密码'
    
) ENGINE=InnoDB DEFAULT CHARSET=utf8;