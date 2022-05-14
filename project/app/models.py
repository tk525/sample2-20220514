from django.db import models
from django.core import validators


class Item(models.Model):

    SEX_CHOICES = (
        (1, '男性'),
        (2, '女性'),
    )

    name = models.CharField(
        verbose_name='名前',
        max_length=200,
    )
#verbose_name　フォーム自動生成で見出しとして使う
#max_lenght　文字長
    age = models.IntegerField(
        verbose_name='年齢',
        validators=[validators.MinValueValidator(1)],
        blank=True,
        null=True,
    )
#verbose_name　フォーム自動生成で見出しとして使う
#validators　バリデーションの追加
#blank　必須入力（デフォはTrue）
    sex = models.IntegerField(
        verbose_name='性別',
        choices=SEX_CHOICES,
        default=1
    )
#verbose_name　フォーム自動生成で見出しとして使う
#choices　選択肢の自動生成
#default　デフォ値
    memo = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )
#verbose_name　フォーム自動生成で見出しとして使う
#max_lenght　文字長
#blank　必須入力（デフォはTrue）
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )
#verbose_name　フォーム自動生成で見出しとして使う
#auto_now_add　追加時に現在時間を設定

    # 以下は管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'
