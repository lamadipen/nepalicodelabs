package com.nepalicodelabs.FormHandling.controller;

import com.nepalicodelabs.FormHandling.model.User;
import jakarta.validation.Valid;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class UserController {
    @GetMapping("/getUserForm")
    public String getUserForm(Model model){
        model.addAttribute("user", new User());
      return "getUserForm";
    }

    @PostMapping("/submitUserForm")
    public String submitFrom(@ModelAttribute @Valid  User user, BindingResult bindingResult, Model model){
        if(bindingResult.hasErrors()){
            return "getUserForm";
        }

        model.addAttribute("user", user);
        return "result";
    }
}
