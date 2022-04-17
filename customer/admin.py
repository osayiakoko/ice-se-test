from django.contrib import admin

from .models import Customer, CustomerPayment


class CustomerPaymentInline(admin.TabularInline):
    model = CustomerPayment
    extra = 1


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    list_filter = ('state',)
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = (CustomerPaymentInline,)


@admin.register(CustomerPayment)
class CustomerPaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'ref_code')
    list_filter = ('payment_type',)
    readonly_fields = ('created_at', 'updated_at')
