package com.nepalicodelabs.MeroSchedular.schedular;

import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import javax.sound.midi.SysexMessage;

@Component
public class MySchedulars {
    @Scheduled(fixedDelay = 5000)
    public void printMyMessage(){
        System.out.println("Schedular is running every 5 seconds");
    }

    @Scheduled(cron = "0 0 * * * *")
    public void printMyMessageCron(){
        System.out.println("Schedular is running via cron expression");
    }

}
