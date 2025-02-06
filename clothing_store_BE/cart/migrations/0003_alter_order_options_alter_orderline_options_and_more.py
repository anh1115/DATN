# Generated by Django 5.1.4 on 2025-01-04 19:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0002_initial"),
        ("products", "0004_alter_banner_options_alter_category_options_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={
                "verbose_name": "Đơn hàng",
                "verbose_name_plural": "Quản lý đơn hàng",
            },
        ),
        migrations.AlterModelOptions(
            name="orderline",
            options={
                "verbose_name": "Chi tiết đơn hàng",
                "verbose_name_plural": "Chi tiết đơn hàng",
            },
        ),
        migrations.AddField(
            model_name="order",
            name="note",
            field=models.CharField(
                blank=True,
                default="",
                max_length=255,
                null=True,
                verbose_name="Ghi chú",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="vnp_BankCode",
            field=models.CharField(blank=True, default="", max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="vnp_BankTranNo",
            field=models.CharField(blank=True, default="", max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="vnp_CardType",
            field=models.CharField(blank=True, default="", max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="vnp_ResponseCode",
            field=models.CharField(blank=True, default="", max_length=2, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="vnp_TransactionNo",
            field=models.CharField(blank=True, default="", max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="vnp_TransactionStatus",
            field=models.CharField(blank=True, default="", max_length=2, null=True),
        ),
        migrations.AddField(
            model_name="orderline",
            name="color",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_lines",
                to="products.color",
                verbose_name="Màu sắc",
            ),
        ),
        migrations.AddField(
            model_name="orderline",
            name="size",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_lines",
                to="products.size",
                verbose_name="Kích cỡ",
            ),
        ),
        migrations.AddField(
            model_name="orderline",
            name="status_review",
            field=models.IntegerField(
                choices=[(0, "Not Reviewed"), (1, "Reviewed")],
                default=0,
                verbose_name="Trạng thái đánh giá",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo"),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_id",
            field=models.CharField(
                max_length=50,
                primary_key=True,
                serialize=False,
                unique=True,
                verbose_name="Mã đơn hàng",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="payment_method",
            field=models.CharField(
                choices=[
                    ("cash_on_delivery", "Tiền mặt"),
                    ("bank_transfer", "Chuyển khoản ngân hàng"),
                ],
                max_length=50,
                verbose_name="Phương thức thanh toán",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Đang chờ xử lý"),
                    ("confirmed", "Đã xác nhận"),
                    ("shipped", "Đã vận chuyển"),
                    ("delivered", "Đã giao"),
                    ("cancelled", "Đã hủy"),
                ],
                max_length=20,
                verbose_name="Trạng thái đơn",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="total_price",
            field=models.DecimalField(
                decimal_places=2,
                default=0.0,
                editable=False,
                max_digits=10,
                verbose_name="Tổng giá trị",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật"),
        ),
        migrations.AlterField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Khách hàng",
            ),
        ),
        migrations.AlterField(
            model_name="orderline",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo"),
        ),
        migrations.AlterField(
            model_name="orderline",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_lines",
                to="cart.order",
                verbose_name="Mã đơn hàng",
            ),
        ),
        migrations.AlterField(
            model_name="orderline",
            name="orderline_id",
            field=models.CharField(
                blank=True,
                editable=False,
                max_length=50,
                primary_key=True,
                serialize=False,
                unique=True,
                verbose_name="Mã dòng đơn hàng",
            ),
        ),
        migrations.AlterField(
            model_name="orderline",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_lines",
                to="products.product",
                verbose_name="Sản phẩm",
            ),
        ),
        migrations.AlterField(
            model_name="orderline",
            name="quantity",
            field=models.PositiveIntegerField(verbose_name="Số lượng"),
        ),
        migrations.AlterField(
            model_name="orderline",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật"),
        ),
    ]
