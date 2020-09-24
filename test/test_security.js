// STUB
test('no alert pop up from malicicious search route q param', () =>{
    // GET search from running server 
    document.location.replace("http://localhost:51618/search?q=1#1' onerror='alert(1);//")
    try {
        expect(data).toBe('peanut butter');
        done();
    } catch (error) {
        done(error);
    }
    
});
