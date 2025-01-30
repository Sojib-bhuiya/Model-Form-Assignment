from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from .forms import MemberForm
from .models import Student
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

class CreateMemberView(CreateView):
    model = Student  # Specify the model
    form_class = MemberForm  # Use the corrected form name
    template_name = 'student_pages/create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Sutudent add Successfully')
        return super().form_valid(form)


class MemberListView(ListView):
    model = Student
    template_name = 'student_pages/home.html'
    context_object_name = 'members'


class MemberUpdateView(UpdateView):
    model = Student
    form_class = MemberForm
    template_name = 'student_pages/create.html'
    pk_url_kwarg = 'id'	
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Modify Info Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context
    

class MemberDeleteView(DeleteView):
    model = Student
    pk_url_kwarg = 'id'
    template_name ='student_pages/delete.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.delete()
        messages.add_message(self.request, messages.SUCCESS, 'Sutudent Delete Successfully')
        return HttpResponseRedirect(success_url)

    # def delete(self, request, *args, **kwargs):
    #     return super().delete(request, *args, **kwargs)