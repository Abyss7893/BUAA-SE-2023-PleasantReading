from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


# Create your models here.
class UserInfo(models.Model):
    userID = models.CharField(max_length=128, null=False, primary_key=True)
    passwd = models.CharField(max_length=32, null=False)
    email = models.EmailField(null=False)
    img = models.ImageField(upload_to='UserImg', default='UserImg/user_img.jpg', verbose_name=u"上传头像")
    gender = models.CharField(max_length=32, null=True)
    nickname = models.CharField(max_length=128, null=True)
    motto = models.CharField(max_length=128, null=True)
    birth = models.DateField(null=True)
    VIPDate = models.DateField(null=True)


class BookBasicInfo(models.Model):
    bookID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False)
    totScore = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    rateNumber = models.IntegerField(default=0)
    author = models.CharField(max_length=128, null=True)
    status = models.CharField(max_length=64, null=False, default='连载')
    onShelf = models.BooleanField(default=True)
    wordsCnt = models.IntegerField(default=0)
    category = models.CharField(max_length=64, null=False)
    profile = models.TextField(null=True)
    img = models.ImageField(upload_to='BookImg', verbose_name=u"图书封面", default='BookImg/default.jpg')
    collections = models.IntegerField()
    isVIP = models.BooleanField(default=False)


class BookContext(models.Model):
    bookID = models.IntegerField(null=False)
    chapter = models.IntegerField()
    title = models.CharField(max_length=128, null=True)
    text = models.TextField(null=False)

    class Meta:
        indexes = [models.Index(fields=['bookID', 'chapter'])]

    # trigger
    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super(BookContext, self).save()
        length = len(self.text)
        pre = BookBasicInfo.objects.get(bookID=self.bookID).wordsCnt
        BookBasicInfo.objects.filter(bookID=self.bookID).\
            update(wordsCnt=pre + length)

# trigger
@receiver(pre_delete, sender=BookContext)
def beforeDeleteCollections(sender, instance, **kwargs):
    length = len(instance.text)
    pre = BookBasicInfo.objects.get(bookID=instance.bookID).wordsCnt
    BookBasicInfo.objects.filter(bookID=instance.bookID). \
        update(pre - length)



class Score(models.Model):
    userID = models.CharField(max_length=128, null=False)
    bookID = models.IntegerField(null=False)
    score = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        indexes = [models.Index(fields=['userID', 'bookID'])]

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super(Score, self).save()
        obj = BookBasicInfo.objects.get(bookID=self.bookID)
        obj.totScore = obj.totScore + self.score
        obj.rateNumber = obj.rateNumber + 1
        obj.save()

    """
        Attention! 
        If you **update** the score, you must update the score in BookBasicInfo by yourself.
        Because I didn't find the signal about pre_update or post_update.
        QWQ 
    """



class Collections(models.Model):
    userID = models.CharField(max_length=128, null=False)
    bookID = models.IntegerField(null=False)

    class Meta:
        indexes = [models.Index(fields=['userID', 'bookID'])]

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super(Collections, self).save()
        collections = BookBasicInfo.objects.get(bookID=self.bookID).collections
        BookBasicInfo.objects.filter(bookID=self.bookID).\
            update(collections=collections+1)

# trigger
@receiver(pre_delete, sender=Collections)
def beforeDeleteCollections(sender, instance, **kwargs):
    obj = BookBasicInfo.objects.get(bookID=instance.bookID)
    obj.collections = obj.collections - 1
    obj.save()



class Comments(models.Model):
    userID = models.CharField(max_length=128, null=False)
    bookID = models.IntegerField(null=False)
    chapter = models.IntegerField(null=False)
    text = models.TextField(null=False)
    timestamp = models.DateField(default='2023-05-24', null=False)
    visible = models.BooleanField(default=True)

    class Meta:
        indexes = [models.Index(fields=['userID', 'bookID', 'chapter'])]



class Bookmark(models.Model):
    userID = models.CharField(max_length=128, null=False)
    bookID = models.IntegerField(null=False)
    chapter = models.IntegerField(null=False)

    class Meta:
        indexes = [models.Index(fields=['userID', 'bookID'])]


class Manager(models.Model):
    userID = models.CharField(max_length=128, null=False)
    passwd = models.CharField(max_length=56, null=False)
    email = models.EmailField(null=False)


class History(models.Model):
    userID = models.CharField(max_length=128, null=False)
    bookID = models.IntegerField(null=False)
    chapter = models.IntegerField(null=False)
    timestamp = models.DateField(null=False)

class Author(models.Model):
    name = models.CharField(max_length=128, primary_key=True)
    img = models.ImageField(upload_to='AuthorImg', verbose_name=u"作者头像", default='AuthorImg/default.jpg')
    profile = models.TextField(default="这个人很懒，什么都没有留下~")
