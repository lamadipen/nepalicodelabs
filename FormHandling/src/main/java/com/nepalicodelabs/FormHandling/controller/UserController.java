package com.nepalicodelabs.FormHandling.controller;

import com.nepalicodelabs.FormHandling.model.User;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
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
    public String submitFrom(@ModelAttribute  User user, Model model){
        model.addAttribute("user", user);
        return "result";
    }
}
