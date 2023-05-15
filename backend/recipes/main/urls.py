from django.urls import path
from . import views

urlpatterns = [

    
    #path('members/details/<int:id>', views.details, name='details'),
    #path('testing/', views.testing, name='testing'),
    path('',views.main,name="main"),
    path('register/',views.register,name="register"),
    path('login/', views.login_view, name = "login"),
    path('logout/',views.logout_view, name = "logout"),
    path('malt_inventory',views.check_stock_malt, name ='malt_inventory'),
    path('hop_inventory',views.check_stock_hop, name ='hop_inventory'),
    path('yeast_inventory',views.check_stock_yeast, name ='yeast_inventory'),
    path('extra_inventory',views.check_stock_extra, name ='extra_inventory'),
    path('remove_malt/<int:malt_id>/', views.remove_malt, name='remove_malt'),
    path('remove_hop/<int:hop_id>/', views.remove_hop, name='remove_hop'),
    path('remove_yeast/<int:yeast_id>/', views.remove_yeast, name='remove_yeast'),
    path('remove_extra/<int:extra_id>/', views.remove_extra, name='remove_extra'),
    path('remove_recipe/<int:recipe_id>/', views.remove_recipe, name='remove_recipe'),
    path('edit_malt/<int:malt_id>/', views.edit_malt, name='edit_malt'),
    path('edit_hop/<int:hop_id>/', views.edit_hop, name='edit_hop'),
    path('edit_yeast/<int:yeast_id>/', views.edit_yeast, name='edit_yeast'),
    path('edit_extra/<int:extra_id>/', views.edit_extra, name='edit_extra'),
    path('edit_recipe/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('recipe_inventory/',views.check_stock_recipe,name='recipe_inventory'),
    path('recipe_detail/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe_detail_read/<int:recipe_id>/', views.recipe_detail_read, name='recipe_detail_read'),
    path('select_malt/<int:recipe_id>/', views.select_malt, name='select_malt'),
    path('remove_recipe_malt/<int:recipe_id>/<int:malt_id>/', views.remove_recipe_malt, name='remove_recipe_malt'),
    path('remove_recipe_brewing/<int:recipe_id>/<int:brewing_id>/', views.remove_recipe_brewing, name='remove_recipe_brewing'),
    path('remove_recipe_boiling/<int:recipe_id>/<int:boiling_id>/', views.remove_recipe_boiling, name='remove_recipe_boiling'),
    path('create_brewing/<int:recipe_id>/', views.create_brewing, name='create_brewing'),
    path('create_boiling/<int:recipe_id>/', views.create_boiling, name='create_boiling'),
    path('add_boiling_hop/<int:boiling_id>/', views.add_boiling_hop, name='add_boiling_hop'),
    path('remove_boiling_hop/<int:recipe_id>/<int:hop_id>/', views.remove_boiling_hop, name='remove_boiling_hop'),
    path('add_boiling_extra/<int:boiling_id>/', views.add_boiling_extra, name='add_boiling_extra'),
    path('remove_boiling_hop/<int:recipe_id>/<int:extra_id>/', views.remove_boiling_extra, name='remove_boiling_extra'),
    path('add_recipe_yeast/<int:recipe_id>', views.add_recipe_yeast, name='add_recipe_yeast'),
    path('remove_recipe_yeast/<int:recipe_id>/<int:yeast_id>/', views.remove_recipe_yeast, name='remove_recipe_yeast'),
    path('remove_recipe_fermentation/<int:recipe_id>/<int:fermentation_id>/', views.remove_recipe_fermentation, name='remove_recipe_fermentation'),
    path('create_fermentation/<int:recipe_id>/', views.create_fermentation, name='create_fermentation'),
    path('recipe_calculations/<int:recipe_id>/', views.recipe_calculations, name='recipe_calculations'),
    path('advanced_edit_recipe/<int:recipe_id>/', views.advanced_edit_recipe, name='advanced_edit_recipe'),
    path('recipe_stock_confirm/<int:recipe_id>/', views.recipe_stock_confirm, name='recipe_stock_confirm'),
    path('recipe_stock/<int:recipe_id>/', views.recipe_stock, name='recipe_stock'),
    path('like_recipe/<int:recipe_id>/', views.like_recipe, name='like_recipe'),
    path('liked_recipes', views.liked_recipes, name='liked_recipes'),
    

]


