form Select location
	text outFolder	 
	text textGridFolder
	text file 
	positive tier 1
endform

Read from file... 'textGridFolder$'/'file$'.TextGrid

#Open TextGrid file in Praat
select TextGrid 'file$'

#Convert to table
Down to Table... no 4 no no

numRows = Get number of rows

Create Table with column names... table numRows tmin tmax phone

for n from 1 to numRows
	select Table 'file$'
	tmin_v = Get value... n tmin
	tmax_v = Get value... n tmax
	phone_v$ = Get value... n text
	select Table table
	Set numeric value... n tmin tmin_v
	Set numeric value... n tmax tmax_v
	Set string value... n phone 'phone_v$'
endfor

select Table table

Save as comma-separated file... 'outFolder$''file$'.lab
	
