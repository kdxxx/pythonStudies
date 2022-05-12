{% extends "layout.html" %}

{% block body %}
<h3> Makaleler </h3>
<hr>
{% if articles %}

<ul class="list-group">
{% for article in articles %}
<li class = "list-group-item"><a href="article/{{article.id}}">{{article.title}}</a></li>
{% endfor %}
</ul>

{% else %}
<div class = "alert alert-danger"> Bu blokta henüz makale yok...</div>
{% endif %}

{% endblock body %}
