mod my{
    pub struct OpenBox <T>{
        pub contents : T,
    }

    pub struct ClosedBox<T>{
        contents : T,
    } 

    impl <T>  ClosedBox<T> {
        pub fn new(contents : T) -> ClosedBox<T>{
            ClosedBox {
                contents : contents,
            }
        }
    }
}


fn main(){
    let openb =  my::OpenBox{contents : "pulbic information"};
    println!("The open box contains, {}" , openb.contents);


    let _clbox = my::ClosedBox::new("classifief info");
}
