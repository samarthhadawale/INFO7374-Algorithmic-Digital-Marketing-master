library(shiny)
library(Cairo)
library(DT)

#load the data in this file to access the name of various columns
dataset <- read.csv(file = "book_data_new.csv", header=T, sep=",")

shinyUI=navbarPage("Predictive Analysis",
                   
                   tabPanel("Frequency",
                            dataTableOutput('Itemcontents'),
                            hr(),
                            
                            list(basicPage(
                              renderTable('Itemcontents')
                            ))
                   ),
                   
                   #UI for Most Frequently Bought Books
                   tabPanel("MFI",
                            fluidPage(
                              titlePanel("Most Frequently Bought Books"),
                              sidebarLayout(
                                sidebarPanel(
                                  sliderInput(inputId = "top_level",label = "Top Items",min=1,
                                              max = 40,value=10), width = 4),
                                mainPanel(plotOutput("ItemGraph"))
                              )
                            )
                   ),
                   
                    tabPanel("Books Sold Mostly With Solaris",plotOutput("avg"))
                     
)

