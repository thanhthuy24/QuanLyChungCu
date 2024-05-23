import { StyleSheet } from "react-native";

export default StyleSheet.create({
    container: {
        flexDirection: 'row',
        flexWrap: 'wrap',
        justifyContent: 'space-between',
        padding: 8,
    },
    cardContainer: {
        width: '48%', // Adjust to fit two items per row, with some spacing
        marginBottom: 8,
    },
    card: {
        flex: 1,
    },
    imageItem: {
        width: 120,
        height: 100
    },
    noneCheck: {
        backgroundColor: 'red',
        color: "white"
    },
    titleItem: {
        fontWeight: "bold",
        fontSize: 18,
        margin: 8
    }, 
    tagItem: {
        width: 150,
        marginBottom: 10        
    },
    alignSelf: {
        alignSelf: "center", 
        marginBottom: 4
    },
    ecabinetStyle: {
        borderColor: '#ddd',  // Màu viền
        borderWidth: 1,       // Độ dày viền
        borderRadius: 5,      // Góc bo tròn viền
        padding: 1,          // Khoảng cách bên trong viền
        marginBottom: 10,     // Khoảng cách giữa các bình luận
        backgroundColor: '#fff', // Màu nền
        marginLeft: 10,
        marginRight: 10,
    }, 
    commentsContainer: {
        marginTop: 10,
    },
});