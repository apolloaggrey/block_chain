var print = function(n)
{
	console.log(n)
}
var print_doc = function(n)
{
	document.write(n)
}
 var factorize =function(n)
 {
 	var result = [];
 	var i = 2;
 	while (n >1)
 	{
 		if (n %i === 0)
 		{
 			n /= i;
 			result.push(i);
 			//print(i);
 		}
 		{
 			i ++;
 		}
 	}
 	return result
 }

//print_doc(factorize(244534))
var numbers = [(1,2,3,4,5,6),[1,2,3,4,5]]
for(i in numbers)//(var i in numbers)
{
	print( numbers[i])
}