from django import forms

from .models import Comment, Tag


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["rating", "text", "guest_name", "guest_email"]
        widgets = {
            "rating": forms.NumberInput(attrs={"min": 1, "max": 5}),
            "text": forms.Textarea(attrs={"class": "form-control form-control-sm", "rows": 3}),
        }

    # Custom validation to ensure guest_name and guest_email are provided for guest users
    def clean(self):
        data = super().clean()
        user = self.initial.get("user")
        if not user and not data.get("guest_name"):
            self.add_error("guest_name", "Required for guest.")
        if not user and not data.get("guest_email"):
            self.add_error("guest_email", "Required for guest.")
        return data


# Form for the Tag model to be used in the ProductAdmin
class TagForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=False
    )

    class Meta:
        model = Tag
        fields = "__all__"
