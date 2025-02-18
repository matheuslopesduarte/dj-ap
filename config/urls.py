"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cadastro.views import EstadoViewSet

from pedidos.views import ClienteViewSet, PedidoViewSet, ItensPedidoViewSet

from biblioteca.views import AlunoViewSet as AlunoBibli, LivroViewSet, EmprestimoViewSet

from hospital.views import PacienteViewSet, MedicoViewSet, ConsultaViewSet

from escola.views import AlunoViewSet, TurmaViewSet, ProfessorViewSet

pedidos_router = DefaultRouter()
pedidos_router.register(r'clientes', ClienteViewSet)
pedidos_router.register(r'pedidos', PedidoViewSet)
pedidos_router.register(r'itens', ItensPedidoViewSet)

biblioteca_router = DefaultRouter()
biblioteca_router.register(r'alunos', AlunoBibli)
biblioteca_router.register(r'livros', LivroViewSet)
biblioteca_router.register(r'emprestimos', EmprestimoViewSet)

hospital_router = DefaultRouter()
hospital_router.register(r'pacientes', PacienteViewSet)
hospital_router.register(r'medicos', MedicoViewSet)
hospital_router.register(r'consultas', ConsultaViewSet)

escola_router = DefaultRouter()
escola_router.register(r'alunos', AlunoViewSet)
escola_router.register(r'turmas', TurmaViewSet)
escola_router.register(r'professores', ProfessorViewSet)

router = DefaultRouter()
router.register(r'estados', EstadoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('pedidos/api/', include((pedidos_router.urls, 'pedidos'))),
    path('biblioteca/api/', include((biblioteca_router.urls, 'biblioteca'))),
    path('hospital/api/', include((hospital_router.urls, 'hospital'))),
    path('escola/api/', include((escola_router.urls, 'escola'))),
]
