from django.contrib import admin
from . models import Customer, Expense


admin.site.site_header = "Expense Tracker"
admin.site.index_title = "Expense Tracker Administration"


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "first_name", "last_name"]
    list_editable = ["first_name", "last_name"]
    list_per_page = 10


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ["customer", "date", "amount", "payment_type"]
    list_editable = ["amount", "payment_type"]
    list_per_page = 10
    list_select_related = ['customer']
