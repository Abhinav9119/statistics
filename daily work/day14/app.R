library(shiny)
ui <- fluidPage(
  selectInput("p","p",choices=names(mtcars)),
  plotOutput("myplot"))
server <- function(input, output, session) {
  output$myplot<-renderPlot({
    boxplot(mtcars[,input$p])
  })
}

shinyApp(ui, server)