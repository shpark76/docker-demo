package com.internship;

import org.apache.commons.lang3.NotImplementedException;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;


@SpringBootApplication
@Controller
public class StartApplication {

    @GetMapping("/")
    public String index(final Model model) {
        model.addAttribute("title", "Docker + Spring Boot");
        model.addAttribute("msg", "Welcome to the docker container! internship<BR>URI: /");
        return "index";
    }

    @GetMapping("/tentative")
    public String skelatonApi(final Model model) {
        model.addAttribute("title", "Docker + Spring Boot");
        model.addAttribute("msg", "Welcome to the docker container! internship<BR>URI: /tentative");
        throw new NotImplementedException("Spring Boot - Not implemented /tentative api");
    }

    public static void main(String[] args) {
        SpringApplication.run(StartApplication.class, args);
    }

}
