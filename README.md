<MTMarkdownOptions output='html4'>
    This is a Mastermind algorithm implementation with constant size memory.
	<br/>
	Here there is a memory restriction for the algorithm, where we are allowed only two strings, viz. x and y in the memory to store our data. 
	<br/>
	The main strategy would be that of figuring the right combination of block string from the x memory and forgetting the data from x memory after that.
	<br><br><br>
	<b>Instructions to run the file : </b>
	<ul>
		<li>
			Put your input file inside the 'input' folder.
		</li>
		<li>
			Run the command "python mastermind.py your_input_file_name" where your_input_file_name is the name of the input file
		</li>	
		<li>
			3 input files are already there in the input folder. So you can run "<b>python mastermind.py input1.txt</b>" , "<b>python mastermind.py input2.txt</b>" and "<b>python mastermind.py input3.txt</b>". 
		</li>	
		<li> 
			input1.txt is a short string where the length is 10 and the number of colors,k = 4.
		</li>	
		<li>
			input2.txt is a very long string where length is 4000 and number of colors, k = 4.
		</li>
		<li>
			input3.txt is a very long string where length is 4000 and number of colors, k = 10.
		</li>
	</ul>
	<br>
	To run the modified algorithm which has an intelligent guess function, run "python mastermind.py &lt;input_file&gt; --n"	
	<br>
	Click <a href="http://en.wikipedia.org/wiki/Mastermind_(board_game)">here</a> to learn more about the original Mastermind game.
</MTMarkdownOptions>




