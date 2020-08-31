class App extends Component{
    constructor(props) {
        super(props)
        this.state = {
            host : 'jesh',
            test :'',
        }
    }

    ComponentDidMount(){
        this._dbDdabong();
    }

    _dbDdabong = async() => {
        const res =await axios.get('/api/ddabong');
        console.log(res.data)
    }

 
    
}