{% extends "layout.html" %}

{% block body %}
<h3> Kontrol Paneli </h3>
<small> Hoş Geldin ,{{session["username"]}}</small>
<hr>

<a href ="/addarticle" class = "btn btn-danger">Makale Ekle</a>

{% if articles %}

<table class="table table-hover">
  <thead>
    <tr>
      <th scope="col">id</th>
      <th scope="col">Başlık</th>
      <th scope="col">Yazar</th>
      <th scope="col">Tarih</th>
      <th scope="col"></th>
      <th scope="col"></th>
    </tr>
  </thead>
  <tbody> 
    {% for article in articles %}
    <tr>
      <th scope="row">{{article.id}}</th>
      <td><a href= "/article/{{article.id}}">{{article.title}}</a> </td>
      <td>{{article.author}}</td>
      <td>{{article.created_date}}</td>
      <td><a href="/edit/{{article.id}}"class = "btn btn-danger"  >Güncelle </a></td>
      <td><a href="/delete/{{article.id}}"class = "btn btn-danger"  >Sil </a></td>

    </tr>
    {% endfor %}



    
 
  </tbody>
</table>

{% else %}
<div class = "alert alert-danger">Henüz makaleniz bulunmuyor...</div>
{% endif %}

{% endblock body %}
