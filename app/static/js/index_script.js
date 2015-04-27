var w = 300, h = 250, padding = 20;
            // Create the SVG
            var svg = d3.select("div.chartinput").append("svg")
                .attr("width", w)
                .attr("height", h)
                .attr("style", "-webkit-tap-highlight-color: #F6F6F6;");

            // Create Axes
            // setup x 
            var xScale = d3.scale.linear().range([padding, w - padding * 2]), // value -> display
                xAxis = d3.svg.axis().scale(xScale).orient("bottom");

            // setup y
            var yScale = d3.scale.linear().range([h - padding, padding]), // value -> display
                yAxis = d3.svg.axis().scale(yScale).orient("left");

            // Add a background
            var rect = svg.append("rect")
                .attr("width", w - padding * 2)
                .attr("height", h - padding * 2)
                .attr("x", padding)
                .attr("y", padding)
                .style("stroke", "#999999");
               // .style("fill", "#F6F6F6");


            // X-Axis
            svg.append("g")
                  .attr("class", "x axis")
                  .attr("transform", "translate(0," + h + ")")
                  .call(xAxis)
                .append("text")
                  .attr("class", "label")
                  .attr("x", w/2)
                  .attr("y", 0)
                  .style("text-anchor", "middle")
                  .text("Form");
            // Y-Axis
            svg.append("g")
                  .attr("class", "y axis")
                  .call(yAxis)
                .append("text")
                  .attr("class", "label")
                  .attr("transform", "rotate(-90)")
                  .attr("x", -h/2)
                  .attr("y", padding/2 + 1)
                  //.attr("dy", ".71em")
                  .style("text-anchor", "middle")
                  .text("Content");


            $(function(){

                var transX;
                var transY;

                // add circle on click
                $("rect").on( "click", function(e) {

                    var circle = svg.selectAll("circle").remove();

                    var posX = e.pageX - $(this).offset().left + padding, 
                        posY = e.pageY - $(this).offset().top + padding;
                    transX = (posX - padding)/(w - padding * 2);
                    transY = 1 - (posY - padding)/(h - padding * 2);

                    // Append a new point
                    svg.append("circle")
                        .attr("transform", "translate(" + posX + "," + posY + ")")
                        .attr("r", "5")
                        .attr("class", "dot")
                        .style("cursor", "pointer");
                    // alert( (transX) + ' , ' + (transY) );

                    // autofocus on submit
                    $('button[type=submit]').focus();
                });
                

                $('button').click(function(){
                    d = 'response_form='+transX+'&response_content='+transY;
                    console.log(d);
                    $.ajax({
                        url: '/signUpUser',
                        data: d,
                        type: 'POST',
                        success: function(response){
                            console.log(response);
                        },
                        error: function(error){
                            console.log(error);
                        }
                    });
                });
            });
