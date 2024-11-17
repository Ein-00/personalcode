package main

import(
	"fmt"
	"sync"
	"time"
)
var wg sync.WaitGroup
type stick struct{sync.Mutex}
type Philo struct{
	number int
	lcs,rcs *stick
}

func (p Philo) eat(ch chan bool){
	for i:= 0;i< 3 ;i++{
		ch <- true
		p.lcs.Lock()
		p.rcs.Lock()
		fmt.Println("Starting to eat.",p.number)
		time.Sleep(time.Second)
		fmt.Println("Finished eating.",p.number)
		p.rcs.Unlock()
		p.lcs.Unlock()
		<-ch
		
		time.Sleep(time.Second)

	}
	wg.Done()
}
func main(){
	cstick := make(	[]*stick, 5)
	for i := 0;i< 5 ;i++{
		cstick[i] = new(stick)
	}
	Philosopher := make([]*Philo, 5)
	for i:= 0;i< 5 ;i++{
		Philosopher[i] = &Philo{
			number : i+1,
			lcs : cstick[i],
			rcs : cstick[(i+1)%5],
		}
	}
	ch := make(chan bool , 2)

	for i := 0;i< 5 ;i++{
		wg.Add(1)
		go Philosopher[i].eat(ch)
	}
	wg.Wait()

}
