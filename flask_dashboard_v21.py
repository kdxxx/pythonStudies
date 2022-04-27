{% extends "layout.html" %}

{% block body %}

<h3> Kontrol Paneli </h3>
<small> Hoş Geldin ,{{session["username"]}}</small>

<hr>

<a href ="/addarticle" class = "btn btn-danger">Makale Ekle</a>

{% endblock body %}
