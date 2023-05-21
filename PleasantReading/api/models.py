from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


# Create your models here.
class UserInfo(models.Model):
    userID = models.CharField(max_length=128, null=False, primary_key=True)
    passwd = models.CharField(max_length=32, null=False)
    email = models.EmailField(null=False)
    img = models.ImageField(upload_to='UserImg', default='user_img.jpg', verbose_name=u"上传头像")
    gender = models.CharField(max_length=32, null=True)
    nickname = models.CharField(max_length=128, null=True)
    motto = models.CharField(max_length=128, null=True)
    birth = models.DateField(null=True)
    VIPDate = models.DateField(null=True)


class BookBasicInfo(models.Model):
    bookID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False)
    totScore = models.DecimalField(max_digits=15, decimal_places=2)
    rateNumber = models.IntegerField()
    author = models.CharField(max_length=128, null=True)
    status = models.CharField(max_length=64, null=False, default='连载')
    onShelf = models.BooleanField(default=True)
    wordsCnt = models.IntegerField(default=0)
    category = models.CharField(max_length=64, null=False)
    profile = models.TextField(null=True)
    img = models.ImageField(upload_to='BookImg', verbose_name=u"图书封面", default='')
    collections = models.IntegerField()
    isVIP = models.BooleanField(default=False)


class BookContext(models.Model):
    bookID = models.ForeignKey('BookBasicInfo', on_delete=models.CASCADE)
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
        BookBasicInfo.objects.filter(bookID=self.bookID).\
            update(wordsCnt=BookBasicInfo.wordsCnt + length)

# trigger
@receiver(pre_delete, sender=BookContext)
def beforeDeleteCollections(sender, instance, **kwargs):
    length = len(instance.text)
    BookBasicInfo.objects.filter(bookID=instance.bookID). \
        update(wordsCnt=BookBasicInfo.wordsCnt - length)



class Score(models.Model):
    userID = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    bookID = models.ForeignKey('BookBasicInfo', on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        indexes = [models.Index(fields=['userID', 'bookID'])]

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super(Score, self).save()
        BookBasicInfo.objects.filter(bookID=self.bookID). \
            update(totScore=BookBasicInfo.totScore + self.score)
        BookBasicInfo.objects.filter(bookID=self.bookID). \
            update(rateNumber=BookBasicInfo.rateNumber + 1)

    """
        Attention! 
        If you **update** the score, you must update the score in BookBasicInfo by yourself.
        Because I didn't find the signal about pre_update or post_update.
        QWQ 
    """



class Collections(models.Model):
    userID = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    bookID = models.ForeignKey('BookBasicInfo', on_delete=models.CASCADE, related_name='BookBasicInfo')

    class Meta:
        indexes = [models.Index(fields=['userID', 'bookID'])]

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super(Collections, self).save()
        BookBasicInfo.objects.filter(bookID=self.bookID).\
            update(collections=BookBasicInfo.collections+1)

# trigger
@receiver(pre_delete, sender=Collections)
def beforeDeleteCollections(sender, instance, **kwargs):
    BookBasicInfo.objects.filter(bookID=instance.bookID). \
        update(collections=BookBasicInfo.collections - 1)



class Comments(models.Model):
    userID = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    bookID = models.ForeignKey('BookBasicInfo', on_delete=models.CASCADE)
    chapter = models.IntegerField(null=False)
    text = models.TextField(null=False)
    visible = models.BooleanField(default=True)

    class Meta:
        indexes = [models.Index(fields=['userID', 'bookID', 'chapter'])]



class Bookmark(models.Model):
    userID = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    bookID = models.ForeignKey('BookBasicInfo', on_delete=models.CASCADE)
    chapter = models.IntegerField(null=False)

    class Meta:
        indexes = [models.Index(fields=['userID', 'bookID'])]


class Manager(models.Model):
    userID = models.CharField(max_length=56, primary_key=True)
    passwd = models.CharField(max_length=56, null=False)
    email = models.EmailField(null=False)


class History(models.Model):
    userID = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    bookID = models.ForeignKey('BookBasicInfo', on_delete=models.CASCADE)
    chapter = models.IntegerField(null=False)
